# Write a Python program to access and print a URL's content to the console.

import urllib.request


def fetch_url_content():
    url = input("Enter the URL: ")

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print("\n--- URL Content ---\n")
            print(content)
    except Exception as e:
        print("Error accessing the URL:", e)

fetch_url_content()