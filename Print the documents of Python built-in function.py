# 	Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function: abs ()
# Expected Result:
# abs(number) -> number
# Return the absolute value of the argument.

def print_docs(func_name):
    try:
        func = eval(func_name)
        print("=" * 50)
        print(func.__doc__)
        print("=" * 50)
    except Exception:
        print("Invalid function name! Please enter a valid built-in function.")


func_name = input("Enter a built-in function name (e.g., abs): ")
print_docs(func_name)