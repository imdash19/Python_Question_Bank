# Write a PYTHON program to split a given list into two parts where the length of the first part of the list is given.
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	Length of the first part of the list: 3
# 	Splited the said list into two parts:
# 	([1, 1, 2], [3, 4, 4, 5, 1])

try:
    lst = [val for val in input("Please enter your elements separated with space: ").split()]
    print("-"*70)
    n = int(input("Length of the first part of the list: "))
    print("-" * 70)
    slst = lst[0:n]
    rlst = lst[n:]

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again.")
    print("-" * 70)

else:
    print("({}, {})".format(slst, rlst))
    print("-" * 70)

finally:print("Program executed successfully.")