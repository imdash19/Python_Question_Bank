#  Write a Python program to create the largest possible number using the elements of a given list of positive integers.
# Original list: [3, 40, 41, 43, 74, 9]
# Largest possible number using the elements of the said list of positive integers: 9744341403
# Original list: [10, 40, 20, 30, 50, 60]
# Largest possible number using the elements of the said list of positive integers: 605040302010
# Original list: [8, 4, 2, 9, 5, 6, 1, 0]
# Largest possible number using the elements of the said list of positive integers: 98654210

def create_largest_number(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if str(lst[i]) + str(lst[j]) < str(lst[j]) + str(lst[i]):
                lst[i], lst[j] = lst[j], lst[i]

    val = ""
    for i in lst:
        val += str(i)

    return int(val)


try:
    ilst = [int(val) for val in input('Please enter your values separated with space: ').split()]
    print("="*60)

    lst = []
    for val in ilst:
        if val >= 0:
            lst.append(val)

except ValueError:
    print("Please enter a number...")

except Exception:
    print("Something went wrong! Please try again...")

else:
    print(f'''Original list: {lst}
Largest possible number using the elements of the said list of positive integers: {create_largest_number(lst)}''')