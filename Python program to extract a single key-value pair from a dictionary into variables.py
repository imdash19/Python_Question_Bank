# Write a Python program to extract a single key-value pair from a dictionary into variables.

def extract_key_value():
    try:
        n = int(input("Enter number of key-value pairs: "))
        user_dict = {}

        for _ in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            user_dict[key] = value

        if len(user_dict) == 0:
            print("Dictionary is empty.")
        else:
            key_var, value_var = next(iter(user_dict.items()))

            print("=" * 50)
            print(f"Extracted Key   : {key_var}")
            print(f"Extracted Value : {value_var}")

    except ValueError:
        print("Invalid input! Please enter valid data.")

extract_key_value()