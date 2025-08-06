# Write a PYTHON program to check if all items of a given list of strings are equal to a given string.

lst = [word for word in input("Please enter your strings with space: ").split()]
print("-"*70)

s = input("Enter your string to check: ")
print("-"*70)

if(len(lst) == 0 or len(s) == 0 or s.isspace()):
    print("Please enter a valid input")
    print("-" * 70)

else:
    for val in lst:
        if(val == s):
            result = True

        else:
            result = False
            break

    print(result)

print("Program executed successfully")