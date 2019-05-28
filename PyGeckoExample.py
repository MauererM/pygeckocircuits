"""
PyGeckoExample.py
GNU GPLv3
Copyright Mario Mauerer 2019
"""

import os
import numpy as np
import matplotlib.pyplot as plt

"""
USER CONFIG:
"""
# The GeckoCIRCUITS simulation file. Make sure to provide an absolute path (this is taken care of by the script below)
SIM_FILE_PATH = "example.ipes"
# Gecko communicates using sockets. Provide a port:
GECKOPORT = 43036
# The example file uses a java-block (see example.ipes) to export simulated data. It creates a file "GeckoExport<N>.txt,
# where <N> is given here:
EXPORT_DATA_FILE_NUM = 1
# In the example, two simulated variables/measurements are exported (they will be added as columns to
# GeckoExport<N>.txt)
NUM_EXPORT_VARS = 2

"""
SCRIPT IMPLEMENTATION:
"""
# Get the current path of GeckoCIRCUITS:
curdir = os.path.dirname(os.path.abspath(__file__))
geckopath = curdir + "/GeckoCIRCUITS/GeckoCIRCUITS.jar"
simfilepath = curdir + "/" + SIM_FILE_PATH

# For java. This must be before the jnius-imports:
os.environ['CLASSPATH'] = geckopath

try:
    from jnius import autoclass

except KeyError:
    # Make sure this knows where java is:
    os.environ['JDK_HOME'] = "/usr/lib/jvm/java-1.8.0-openjdk-amd64"
    os.environ['JAVA_HOME'] = "/usr/lib/jvm/java-1.8.0-openjdk-amd64"
    from jnius import autoclass

# The class to control GeckoCIRCUITS:
Inst = autoclass('gecko.GeckoRemoteObject')
# Note that parameters must be passed as java-strings to Gecko, as it otherwise throws a fit:
JString = autoclass('java.lang.String')

# Start GeckoCIRCUITS. This opens the Gecko window:
ginst = Inst.startNewRemoteInstance(GECKOPORT)

# Open the simulation file. Use java-strings:
print(simfilepath)
fname = JString(simfilepath)
ginst.openFile(fname)

# Set the global parameters in the simulation file: These parameters must be defined in Tools->Set Parameters in
# the GUI.
# This is how the simulation file can be adapted/scripted.
parname = JString("$ampl")
ginst.setGlobalParameterValue(parname, 55.0)

# The desired number of the export-file:
parname = JString("$fileNum")
ginst.setGlobalParameterValue(parname, EXPORT_DATA_FILE_NUM)

# Set the number of variables to export (see the "export"-java-block in the simulation file):
parname = JString("$numVar")
ginst.setGlobalParameterValue(parname, NUM_EXPORT_VARS)

ginst.set_dt(200e-9)  # Simulation time step
ginst.set_Tend(5e-3)  # Simulation time
# No pre-simulation:
ginst.set_dt_pre(0)
ginst.set_Tend_pre(0)

ginst.runSimulation()  # Run the simulation. This creates GeckoExport<N>.txt in the current directory
ginst.shutdown()  # Close GeckoCIRCUITS. The data is stored in GeckoExport<N>.txt during the simulation.

# Import the generated data:
exp_fname = "GeckoExport" + "%d" % EXPORT_DATA_FILE_NUM + ".txt"
data = np.genfromtxt(exp_fname, delimiter=',', skip_header=1, usecols=range(0, NUM_EXPORT_VARS + 1))
time = data[:, 0]  # This is always given
# Two variables were exported:
val_1 = data[:, 1]
val_2 = data[:, 2]

# Plot the data:
fig, ax = plt.subplots()
ax.plot(time, val_1, color='r', label='val_1')
ax.plot(time, val_2, color='b', label='val_2')
plt.legend(loc='best')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Exported Data')
ax.grid()
plt.show()
