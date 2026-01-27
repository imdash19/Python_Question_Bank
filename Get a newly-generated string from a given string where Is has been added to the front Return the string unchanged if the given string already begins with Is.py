# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

def generate_new_string(string):
    if string.startswith("Is"):
        return string
    else:
        return "Is " + string

user_input = input("Enter a string: ")
print(generate_new_string(user_input))