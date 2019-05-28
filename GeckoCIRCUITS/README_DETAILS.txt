GeckoCIRCUITS was released as open source (GPL v3) in Nov. 2018 on Sourceforge: https://sourceforge.net/projects/geckocircuits/
It is released as a netbeans project.
The released Gecko does not require a license to run.
Java 8 is used (must be used). Make sure it's also set as the system's default java.
Java >8 does not work, as there are some (java-related) errors.
Some hacks and build-script adaptations were needed to get netbeans running.
The manifest of the generated .jar was modified manually to operate properly, using manifest information from the Gecko binary available at http://gecko-simulations.com/geckocircuits.html (which requires a license to run).
The libraries (and manifest and defaultProperties.prp) were taken from that original Gecko (Which is still available on the GeckoCIRCUTIS homepage), as
Netbeans did not include them in the /dist/lib folder.
tools_180.jar is used (in the /lib folder)
