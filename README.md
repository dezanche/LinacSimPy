# LinacSimPy
![Static Badge](https://img.shields.io/badge/Python-stuff?style=flat&logo=python&color=lime)\
Medical linear accelerators (LINACs) are machines that use electron beams to deliver ionizing radiation to treat tumours and other medical conditions.
LinacSimPy is an interactive model of a linac meant for use in educational programs for medical physicists, radiation therapists and service personnel.
It simulates how the operating parameters of a linac affect measurable properties of the output beam such as dose rate, symmetry, and uniformity.

![LinacSimPy windows](/resources/images/LinacSimPy_collage.png)

# Running LinacSimPy
LinacSimPy is supplied as Python source code to ensure it is compact, portable and can be modified. Despite not being an executable, it's *very easy* to install and should run on anything that can run Python.

The basic capabilities of LinacSimPy are described in [this YouTube video](https://www.youtube.com/watch?v=l84XlGtHGhk).

## Requirements
LinacSimPy requires Python 3.* and has been tested under both Windows and Linux. It uses several standard packages that are listed in `requirements.txt`.
Unless you are using Python for other work and need additional functionality, the installers from the [Python Software Foundation](https://www.python.org/) are sufficient.
You must ensure that all the required packages are present by running `pip install -r requirements.txt` or the equivalent command for your Python distribution (e.g., Conda in Anaconda).

## Installation
Download the archive as a `zip file` (**Code > Download Zip** in the menu above or click [here](https://github.com/dezanche/LinacSimPy/archive/refs/heads/main.zip)) and extract it to a suitable (empty) directory on your machine. You can also use the `git clone` command if you have `git` installed on your system.


## Usage
From the command line prompt (`CMD` terminal in Windows) `cd` to the directory where you saved the LinacSimPy archive. On a correctly-configured system executing `python LinacSimPyMain.py` (or `python3...`) from the command line should launch the program and display the main window. The first time you do this may take a few seconds while Python creates the `*.pyc` files.

If the system cannot find Python in its search `path` you'll get an error (or Windows launches the Microsoft Store app). There are many guides online on how to fix this by adding Python to your `path`. Alternatively you can specify the complete path to the Python executable like this example on Windows:

```>C:\Program Files\Python310\python LinacSimPyMain.py```

## Feedback
Please report bugs, post comments and questions by creating an [issue](https://github.com/dezanche/LinacSimPy/issues) (see above).

# Version History

## Credits
LinacSimPy is based on SIMAC version 3.4, by Marco Carlone, Miller MacPherson, Rhys Anderson, Michael Lamey, and Kevin Wang.\
Theory and technical details of SIMAC were published in [JACMP, Vol. 16, No. 3, 2015](https://doi.org/10.1120%2Fjacmp.v16i3.5139).

## Changelog
This is a brief summary of the changes made to obtain LinacSimPy:
- ported PyQt4 calls to corresponding calls in PyQt5
- various fixes to update from Python 2.7 to 3.10, to matplotlib 3.10.0
- added tooltips to buttons
- added keyboard shortcuts to common operations
- toggle color (red, green) of beam on/off button depending on state
- added confirmation dialog before closing
- added splash screen at startup
- added information message when calculating without beam on and energy selected (idle)
- turning off linac no longer resets energy and values
- replaced copyrighted images with cc-by versions and added tooltips to original file when hovering over
- changed name to LinacSimPy
- layout changes to accommodate longer labels for clarity
- changed `us` to use the proper micro symbol, i.e., $\mu$

## Known Issues
- windows and items inside are not resizable
- input and output quantities are not grouped clearly in the main window
- general layout of the main window can be improved
- input values can be entered only using the sliders, not with the text boxes
- cannot reset to default state without restarting 
- grid voltage control is disabled
- some operations in the File menu cause a crash

# Legal Statements

## Copyright

© 2025 Alberta Health Services, Medical Physics

![GPLv3](/resources/images/gplv3-or-later.png)\
LinacSimPy is free software: you can redistribute it and/or modify it under the terms of the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html) as published by the Free Software Foundation, either version 3 of the License, or any later version.\
LinacSimPy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html) for more details.

![CClicense](https://i.creativecommons.org/l/by-nd/4.0/88x31.png)\
All other original content in this repository (including this README file) is licensed under a [Creative Commons Attribution-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nd/4.0/).

## Disclaimer

This material is intended for general information only and is provided on an "as is", "where is" basis. Although reasonable efforts were made to confirm the accuracy of the information, Alberta Health Services does not make any representation or warranty, express, implied or statutory, as to the accuracy, reliability, completeness, applicability or fitness for a particular purpose of such information. This material is not a substitute for the advice of a qualified health professional. Alberta Health Services expressly disclaims all liability for the use of these materials, and for any claims, actions, demands or suits arising from such use.



