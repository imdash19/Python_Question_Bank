# Write a Python program to check whether multiple variables have the same value.

def check_same_values():
    values = input("Enter values separated by space: ").split()
    processed_values = []
    for val in values:
        try:
            processed_values.append(int(val))
        except ValueError:
            processed_values.append(val)

    if all(x == processed_values[0] for x in processed_values):
        print("All variables have the SAME value.")
    else:
        print("Variables have DIFFERENT values.")

check_same_values()