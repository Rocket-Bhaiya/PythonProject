import cx_Freeze
import sys
import os
base = None
if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base,icon="profile.ico")]

cx_Freeze.setup(
    name = "Login System",
    options = {"build_exe": {"packages":["tkinter","os","sys"], "include_files":['tcl86t.dll','tk86t.dll','profile.ico','image']}},
    version = "1.0",
    description = "Login And Signup UserProfile System | Developed by Abhishek Patel",
    executables = executables
    )
