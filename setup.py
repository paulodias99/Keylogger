import sys
from cx_Freeze import setup, Executable
from random import randint
import time


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("KeyLogger.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["time", "randint"],
        include_files = [],
        excludes = []
)




setup(
    name = "KeyLogger",
    version = "1.0",
    description = "KeyLogger Desenvolvido em Python",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
