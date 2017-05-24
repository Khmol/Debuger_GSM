# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt5. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# Run the build process by running the command
#
# C:\Python34\python.exe setup.py build_exe
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys, os.path
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable( os.path.abspath('Debuger_GSM.py'), base = base, icon = 'touchscreen.ico')
]

setup(name='Debuger_GSM',
      version='1.0',
      description='Debuger_GSM',
      options=options,
      executables=executables
      )
