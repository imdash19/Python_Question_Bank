# Write a Python program to convert true to 1 and false to 0.

def convert_boolean():
    try:
        user_input = input("Enter True or False: ").strip().capitalize()

        if user_input not in ["True", "False"]:
            print("Invalid input! Please enter True or False.")
            return
        bool_value = user_input == "True"
        int_value = int(bool_value)

        print("=" * 40)
        print(f"Boolean value : {bool_value}")
        print(f"Integer value : {int_value}")

    except Exception as e:
        print("Error:", e)

convert_boolean()