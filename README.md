# LinacSimPy
Medical linear accelerators (LINACs) are machines that deliver doses of ionizing radiation to treat tumours and other medical conditions.
LinacSimPy is an interactive model of a linac for educational purposes. It simulates how the operating parameters of a linac affect measurable properties of the output beam such as dose rate, symmetry, and uniformity.
Typical users of LinacSimPy include teaching programs for medical physicists, radiation therapists and service personnel.

![LinacSimPy windows](/resources/images/LinacSimPy_collage.png)

# Running LinacSimPy
LinacSimPy is supplied as Python source code to ensure it's portable. Despite not being an executable, it's *very easy* to install and should run on anything that can run Python.

## Requirements
LinacSimPy requires Python 3.* and has been tested under both Windows and Linux. It uses several standard packages that are listed in `requirements.txt`.
Unless you are using Python for other work and need additional functionality, the installers from the [Python Software Foundation](https://www.python.org/) are sufficient.
You must ensure that all the required packages are present by running `pip install requirements.txt` or the equivalent command for your Python distribution (e.g., Conda in Anaconda).

## Installation
Download the archive as a `zip file` and extract it to a suitable (empty) directory on your machine. You can also use the `git clone` command if you have `git` installed on your system.


## Usage
From the command line (`CMD` terminal in Windows) `cd` to the directory where you saved the LinacSimPy archive. On a correctly-configured system running `python LinacSimPyMain.py` should launch the program and display the main window. The first time you do this may take a few seconds while Python creates the `*.pyc` files.

If the system cannot find Python in its search `path` you'll get an error (or Windows launches the Microsoft Store app). There are many guides online on how to fix this by adding Python to your `path`. Alternatively you can specify the complete path to the Python executable like this example on Windows:

```>C:\Program Files\Python310\python LinacSimPyMain.py```



# Version History

## Credits

## Changelog

# Licenses

