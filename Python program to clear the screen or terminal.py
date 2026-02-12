# Write a Python program to clear the screen or terminal.

import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')

input("Press Enter to clear the screen...")
clear_screen()
print("Screen Cleared Successfully!")