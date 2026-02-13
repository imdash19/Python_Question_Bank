# Write a Python program to get system command output.

import subprocess

def get_command_output():
    command = input("Enter the system command: ")

    try:
        result = subprocess.run(command,
                                shell=True,
                                capture_output=True,
                                text=True)

        print("\n--- Command Output ---\n")
        print(result.stdout)

        if result.stderr:
            print("\n--- Errors ---\n")
            print(result.stderr)

    except Exception as e:
        print("Error executing command:", e)

get_command_output()