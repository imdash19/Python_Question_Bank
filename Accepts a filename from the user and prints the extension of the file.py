# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename: abc.java
# Output: java

filename = input("Please enter a filename: ")

if '.' in filename and not filename.startswith('.'):
    extension = filename.rsplit('.', 1)[-1]
    print(extension)
else:
    print("No extension found")