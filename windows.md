### Windows package for better installation experience

# Path: windows.md
### Windows package for better installation experience

## Installation

### Install from Chocolatey

```bash 
pip install pyinstaller

# Now you can use pyinstaller to build your application

pyinstaller --onefile yourscript.py

# it will create a folder dist with your executable inside it.You can distribute this executable file to your Windows users, and they can run it without needing to install any dependencies or set up a Python environment

# If you want to create a .exe file, you can use the following command

pyinstaller --onefile --windowed yourscript.py

# The --windowed option will hide the console window when the application is running

```
## [dist](/flask/dist/app) folder contains the executable file.

