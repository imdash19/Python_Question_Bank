# Write a Python program to get the Identity, Type, and Value of an object.

def object_details():
    print("=" * 60)
    print("Get Identity, Type, and Value of an Object")
    print("=" * 60)

    user_input = input("Enter a value (number, string, list, etc.): ")

    try:
        obj = eval(user_input)
    except:
        obj = user_input

    print("\nObject Details:")
    print("-" * 60)
    print("Value      :", obj)
    print("Type       :", type(obj))
    print("Identity   :", id(obj))
    print("-" * 60)


object_details()