# Write a Python program to validate an IP address.

import re

def validate_ip():
    ip = input("Enter an IP address: ").strip()
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}" \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"

    if re.match(pattern, ip):
        print("=" * 50)
        print(f"{ip} is a VALID IPv4 address ✅")
    else:
        print("=" * 50)
        print(f"{ip} is NOT a valid IPv4 address ❌")

validate_ip()