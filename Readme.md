# Ubuntu/Debian deb package for better installation of any software

## Lets take a sample flask app

```python
from flask import Flask
import datetime
import platform

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/info")
def info():
    #color the output
    return "This is a Flask app running on " + platform.system() + "."

@app.route("/time")
def time():
    return "The current time is " + str(datetime.datetime.now()) + "."

if __name__ == "__main__":
    app.run(host='', port=8080)

```

## Create a virtual environment

```bash
python3 -m venv venv
```

## Activate the virtual environment

```bash
source venv/bin/activate
```

## Install the required packages

```bash
pip install -r requirements.txt
```

## Create a deb package

### Step 1: Create a directory structure


```bash
# Make a directory named flask-app-deb-1.0.0

mkdir flask-app-deb-1.0.0
cd flask-app-deb-1.0.0

# Install dh_make to create the debian package

sudo apt install dh-make
dh_make -s --createorig

# under DEBIAN directory, create a file named control(skip this step if you are using dh_make)

touch DEBIAN/control

## Add the following content to the control file
Source: myflaskapp
Section: web
Priority: optional
Maintainer: Your Name <youremail@example.com>
Build-Depends: debhelper (>= 9)
Standards-Version: 3.9.5

Package: myflaskapp
Architecture: all
Depends: python, python-flask
Description: A simple Flask web application
 This is a simple Flask web application that demonstrates how to use the Flask web framework.


# Create a directory named usr and under it create a directory named local

mkdir -p usr/local

# Create a directory named myflaskapp under usr/local

mkdir -p usr/local/myflaskapp

# Copy the flask app and requirements.txt to the myflaskapp directory

cp -r ../myflaskapp/* usr/local/myflaskapp

# Create a directory named bin under usr/local

mkdir -p usr/local/bin

# Create a file named myflaskapp under bin

touch usr/local/bin/myflaskapp

## Add the following content to the myflaskapp file
#!/bin/bash
cd /usr/local/myflaskapp
source venv/bin/activate
python app.py

# Make the myflaskapp file executable

chmod +x usr/local/bin/myflaskapp

# Create a directory named etc and under it create a directory named systemd


mkdir -p etc/systemd/system


# Create a file named myflaskapp.service under systemd

touch etc/systemd/system/myflaskapp.service

## Add the following content to the myflaskapp.service file
[Unit]
Description=My Flask App
After=network.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/usr/local/myflaskapp
ExecStart=/usr/local/bin/myflaskapp
Restart=on-failure


[Install]
WantedBy=multi-user.target

# Create a file named postinst under DEBIAN

touch DEBIAN/postinst

## Add the following content to the postinst file
#!/bin/bash
systemctl daemon-reload
systemctl enable myflaskapp
systemctl start myflaskapp


# Make the postinst file executable

chmod +x DEBIAN/postinst

# Create a file named prerm under DEBIAN

touch DEBIAN/prerm

## Add the following content to the prerm file
#!/bin/bash
systemctl stop myflaskapp
systemctl disable myflaskapp


# Make the prerm file executable

chmod +x DEBIAN/prerm

# Create a file named postrm under DEBIAN

touch DEBIAN/postrm

## Add the following content to the postrm file
#!/bin/bash
systemctl daemon-reload


# Make the postrm file executable

chmod +x DEBIAN/postrm

# Create a file named changelog under DEBIAN

touch DEBIAN/changelog

## Add the following content to the changelog file

myflaskapp (1.0.0) unstable; urgency=low

  * Initial release.

 -- Your Name <
    

# Create a file named compat under DEBIAN

touch DEBIAN/compat

## Add the following content to the compat file

9

# Create a file named rules under DEBIAN

touch DEBIAN/rules

## Add the following content to the rules file

#!/usr/bin/make -f
%:
    dh $@

# Make the rules file executable

chmod +x DEBIAN/rules

# Create a file named myflaskapp.install under DEBIAN

touch DEBIAN/myflaskapp.install

## Add the following content to the myflaskapp.install file

usr/local/bin/myflaskapp usr/local/bin
usr/local/myflaskapp usr/local
etc/systemd/system/myflaskapp.service etc/systemd/system

# Create a file named myflaskapp.docs under DEBIAN

touch DEBIAN/myflaskapp.docs

## Add the following content to the myflaskapp.docs file

usr/local/myflaskapp/README.md usr/share/doc/myflaskapp

# Create a file named myflaskapp.docs under DEBIAN

touch DEBIAN/myflaskapp.docs





