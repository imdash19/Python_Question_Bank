# Write a Python program to display some information about the OS where the script is running.

import os
import platform
import socket

def display_os_info():

    print("\n" + "=" * 60)
    print("Operating System Information")
    print("=" * 60)

    print(f"OS Name              : {os.name}")
    print(f"Platform System      : {platform.system()}")
    print(f"Platform Release     : {platform.release()}")
    print(f"Platform Version     : {platform.version()}")
    print(f"Machine Type         : {platform.machine()}")
    print(f"Processor            : {platform.processor()}")
    print(f"Architecture         : {platform.architecture()[0]}")
    print(f"Hostname             : {socket.gethostname()}")
    print(f"Current Working Dir  : {os.getcwd()}")
    print(f"Python Version       : {platform.python_version()}")

    print("=" * 60)

display_os_info()