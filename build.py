import os
import platform
import subprocess

if platform.system() == "Darwin":
    icon = "./resources/codepad.icns"
else:
    icon = "./resources/codepad.ico"

subprocess.run(
    [
        "pyinstaller",
        "./codepad/__main__.py",
        "--windowed",
        "--name",
        "Codepad",
        "--icon",
        icon,
        "--add-data",
        f"./resources/codepad.png{os.path.pathsep}./resources/",
        "--exclude-module",
        "_bootlocale",
    ]
)
