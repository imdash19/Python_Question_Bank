# Write a PYTHON program to remove key values pairs from a list of dictionaries.

keyval = [val for val in input("Please enter the key names with space: ").split()]
print("-"*70)
print(keyval, len(keyval))
print("-"*70)

value = [val for val in input("Please enter the values with space: ").split()]
print("-"*70)
print(value, len(value))
print("-"*70)

if(len(keyval) != len(value)):
    print("Values of both the list should be same")
    print("-" * 70)

else:
    lst = []
    d = {}
    for val1, val2 in zip(keyval, value):
        d[val1] = val2

    lst.append(d)
    print(lst)
    print("-"*70)

    rkey = input("Please enter the index value of key: ")
    print("-" * 70)
    d.pop(rkey)
    print(lst)
    print("-" * 70)

print("Program executed successfully")