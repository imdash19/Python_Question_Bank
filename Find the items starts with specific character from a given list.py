# Write a PYTHON program to find the items starts with specific character from a given list.
# 		Expected Output:
# 		Original list:
# 		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# 		Items start with a from the said list:
# 		['abcd', 'abc', 'acjd']
# 		Items start with d from the said list:
# 		['dagfa']
# 		Items start with w from the said list:
# 		[]

try:
    result = []
    lst = [item for item in input("Please enter your items separated by space: ").split()]
    print("-"*70)

    s = input("Please enter the specific character: ")
    print("-" * 70)

    if(len(lst) == 0 or s.isspace()):
        print("Please enter a valid input.")
        print("-" * 70)

    else:
        n = len(s)
        for val in lst:
            if(val[0:n] == s):
                result.append(val)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again.", e, type(e))
    print("-" * 70)

else:
    print("Items start with {} from the list: {}".format(s, result))
    print("-" * 70)

finally:
    print("Program executed successfully")