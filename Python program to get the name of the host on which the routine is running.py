# Write a Python program to get the name of the host on which the routine is running.

import socket

def get_host_name():
    host_name = socket.gethostname()
    return host_name

print("Host Name:", get_host_name())