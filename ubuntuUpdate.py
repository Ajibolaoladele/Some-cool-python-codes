# Written by Brad Penney, January 2018
# Must be run as "sudo" - sudo python ubuntuUpdate.py
# Updates, upgrades and autoremoves all software packages in Ubuntu 16.04

import subprocess

# check for updates
subprocess.call("apt update",shell=True)

# apply upgrades
subprocess.call("apt upgrade -y",shell=True)

# autoremove packages no longer used
subprocess.call("apt autoremove -y", shell=True)
