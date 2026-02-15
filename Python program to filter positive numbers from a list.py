# Write a Python program to filter positive numbers from a list.

def filter_positive_numbers():
    try:
        lst = [int(val) for val in input(
            'Please enter your values separated with space: '
        ).split()]
        print("=" * 60)

    except ValueError:
        print("Error: The input contains non-numeric values.")
        return []

    else:
        positive_list = []
        for val in lst:
            if val > 0:
                positive_list.append(val)
        return positive_list

result = filter_positive_numbers()
print("Positive numbers:", result)