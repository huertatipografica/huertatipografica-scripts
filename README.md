# ABOUT

These are Python scripts for use with the [Glyphs font editor](http://glyphsapp.com/).


# INSTALLATION

Put the scripts into the *Scripts* folder which appears when you choose *Open Scripts Folder* from the *Scripts* menu.

For some scripts, you will also need to install Tal Leming's *Vanilla*. Here's how. Open Terminal and copy and paste the following lines and hit return. You can copy all of them at once. Notes: the second line (`curl`) may take a while, the `sudo` line will prompt you for your password (type it and press Return, you will *not* see bullets):

    cd ~/Library/
    curl http://download.robofab.com/RoboFab_599_plusAllDependencies.zip > robofab.zip
    unzip -o robofab.zip -d Python_Installs
    rm robofab.zip
    cd Python_Installs/Vanilla/
    sudo python2.6 setup.py install
	

And you are done. The installation should be effective immediately, but in case it does not work right away, you may want to restart your Mac or log out and back in again.


# License

Copyright 2011-2014 Huerta Tipográfica (http://www.huertatipografica.com / @huertatipo).
Some code made thank to Georg Seifert (@schriftgestalt) and Eric Rainer (@mekkablue) help.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use the software provided here except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
