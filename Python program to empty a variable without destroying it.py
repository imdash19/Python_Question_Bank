# Write a Python program to empty a variable without destroying it.
# Sample data: n=20
# d = {"x":200}
# Expected Output: 0
# {}

def empty_variable():
    value = input("Enter a value (number or dictionary like {'x':200}): ")

    try:
        n = int(value)
        print("Before emptying:", n)
        n = type(n)()
        print("After emptying:", n)

    except ValueError:
        try:
            d = eval(value)
            if isinstance(d, dict):
                print("Before emptying:", d)

                d.clear()
                print("After emptying:", d)
            else:
                print("Unsupported data type.")
        except:
            print("Invalid input format.")

empty_variable()