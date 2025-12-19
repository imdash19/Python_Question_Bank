# Write a Python program to build a list, using an iterator function
# and an initial seed value.
# Sample Output: [-10, -20, -30, -40]

def list_initial_seed(sv, itr, e):
    olst = []

    for i in range(e):
        olst.append(sv)
        sv = sv + itr

    return olst


try:
    sv = int(input("Enter the initial seed value: "))
    itr = int(input("Enter the iterator value: "))
    e = int(input("Number of elements: "))

    if e <= 1:
        raise ValueError

except ValueError:
    print('Please enter valid integer values (elements >= 2)...')

else:
    print(f'''Sample Output: {list_initial_seed(sv, itr, e)}''')