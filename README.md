Archive Image Extractor
Description

This Python script searches for image files (.png, .jpg, .bmp, .gif) within compressed archives (.zip, .rar, .7z) in a given directory. It inspects each archive and extracts only the relevant image files. If multiple images are found in a single archive, they are renamed sequentially with a number suffix.
Requirements

    Python 3.6+
    zipfile36, rarfile, py7zr Python libraries

Installation

First, install the required Python libraries using pip:

pip install zipfile36 rarfile py7zr

Adding unrar to PATH

For the script to handle .rar files, the unrar utility needs to be installed and accessible in your system's PATH.
Windows

    Download unrar from the Rarlab website.
    Extract the downloaded file and place unrar.exe in a directory.
    Add the directory path to your system's PATH:
        Open the Start Menu and search for "Environment Variables".
        Click on "Edit the system environment variables".
        In the System Properties window, click on the "Environment Variables" button.
        Under "System variables", find and select the Path variable, then click "Edit".
        Click "New" and add the directory path where unrar.exe is located.
        Click "OK" to close all windows.

macOS

    Install unrar using Homebrew:

    brew install unrar

Linux

    Install unrar using your package manager. For example, on Debian-based systems:

    sudo apt-get install unrar

Usage

Run the Python script and follow the prompts to specify the directory containing the archives and the directory where extracted images should be saved:

python zippic.py

This README provides installation instructions for the required Python libraries and a detailed walkthrough for adding unrar to the PATH on different operating systems.
