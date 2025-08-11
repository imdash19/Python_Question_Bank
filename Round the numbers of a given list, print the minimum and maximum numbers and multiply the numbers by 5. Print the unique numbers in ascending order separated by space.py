# Write a PYTHON program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
# 	Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# 	Minimum value: 4
# 	Maximum value: 22
# 	Result: 20 25 45 55 60 70 80 90 110

try:
    lst = [float(val) for val in input("Please enter your values separated with space: ").split()]
    print("-"*70)

    result = []
    for ele in lst:
        value = 5 * round(ele)
        result.append(value)
    result.sort()

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please try again.", e)
    print("-" * 70)

else:
    print("Original list: ", lst)
    print("-" * 70)
    print("Minimum value: ", int(min(lst)))
    print("-" * 70)
    print("Maximum value: ", int(max(lst)))
    print("-" * 70)
    print("Result: ", result)
    print("-" * 70)

finally:
    print("Program executed successfully.")