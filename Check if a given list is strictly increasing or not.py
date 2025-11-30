# Write a Python program to check if a given list is strictly increasing or not.

try:
    lst = [int(val) for val in input("Please enter your values separated with space: ").split()]
    print("="*60)

    is_increasing = True

    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            print(f"List is NOT strictly increasing because {lst[i]} >= {lst[i+1]} at positions {i} and {i+1}.")
            is_increasing = False
            break

    if is_increasing:
        print("True — The list is strictly increasing.")

except ValueError:
    print("Please enter valid numbers only...")

except Exception:
    print("Something went wrong! Try again later...")