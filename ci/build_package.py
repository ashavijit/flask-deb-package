import os 

def build_package():
    # Build the package
    os.system("git clone https://github.com/ashavijit/flask-deb-package")
    os.chdir("flask-deb-package")

   # create the debian package skeleton
    os.system("dh-make -s --createorig -p flask-deb-package")

    # Edit the debian/control file
    with open("flask-app-deb-1.0/debian/control", "w") as f:
        f.write('Source: myproject\n')
        f.write('Section: utils\n')
        f.write('Priority: optional\n')
        f.write('Maintainer: Your Name <youremail@example.com>\n')
        f.write('Build-Depends: debhelper (>= 9)\n')
        f.write('\n')
        f.write('Package: myproject\n')
        f.write('Architecture: all\n')
        f.write('Depends: python3\n')
        f.write('Description: A short description of your package\n')
        f.write(' A longer description of your package\n')

    # Edit the debian/rules file

    with open("flask-app-deb-1.0/debian/rules", "w") as f:
        f.write('#!/usr/bin/make -f\n')
        f.write('%:\n')
        f.write('\tdh $@\n')

    # Build the package
    os.system("dpkg-buildpackage -us -uc")

    # Install the package

    os.system("sudo dpkg -i ../myproject_1.0_all.deb")

    # Run the package

    os.system("myproject")

    build_package()