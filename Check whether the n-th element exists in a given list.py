# Write a PYTHON program to check whether the n-th element exists in a given list.

lst = [val for val in input("Please enter your list elements with space: ").split()]
print("-"*70)

n = int(input("Please enter the index number for check: "))
print("-"*70)

try:
    if(n >= 1):
        if (lst[n - 1] in lst):
            print("Present in list, ", lst[n - 1])
            print("-" * 70)

    else:
        if (lst[n] in lst):
            print("Present in list, ", lst[n])
            print("-" * 70)

except IndexError:
    print("Not present in list")
    print("-" * 70)

finally:
    print("Program executed successfully")