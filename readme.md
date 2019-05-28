# PyGeckoCIRCUITS
##### Python-Wrapper for GeckoCIRCUITS

GeckoCIRCUITS is a fast and open-source circuit simulator optimized for switch-mode power electronics simulations (and much more). It offers a powerful, java-based programming interface, which renders it highly flexible and versatile.

GeckoCIRCUITS is released under GPLv3 here: https://sourceforge.net/projects/geckocircuits/

Its original homepage is here: http://gecko-simulations.com/geckocircuits.html

This repository contains a simple example that shows how Python (3) can be used to interface/control GeckoCIRCUITS. This is especially suitable for parametric circuit simulations and/or optimizations. Linux (Ubuntu) was used for testing. Java 8 is required.

The example consists of a Python script and a simulation file (.ipes). There is a dedicated java-block in the gecko simulation that exports a (configurable) number of simulated variables/measurements to a text file, which can then be further processed. Global simulation parameters are used to adjust the simulation with the Python script.  

Note that this project contains a reduced set of the GeckoCIRCUITS simulator/source. The full code can be found at https://sourceforge.net/projects/geckocircuits/
The GeckoCIRCUITS found in this project was recompiled from the (open) source, and the resulting .jar is given in this project.

This project is under the same license conditions as GeckoCIRCUITS: GPLv3.

Run PyGeckoExample.py with Python3 to execute the example.

GeckoCIRCUITS can also be operated stand-alone: java -jar GeckoCIRCUITS.jar.
