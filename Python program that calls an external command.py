# Python program that calls an external command.

import subprocess

def run_command():
    command = input("Enter the command to run: ")

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        print("\n--- Output ---")
        print(result.stdout)

        if result.stderr:
            print("\n--- Error ---")
            print(result.stderr)

    except Exception as e:
        print("Error:", e)

run_command()