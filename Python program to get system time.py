# Write a Python program to get system time.
# Note: The system time is important for debugging, network information, random number seeds, or something as simple as program performance.

import time
def get_system_time():
    return time.ctime()

print(get_system_time())