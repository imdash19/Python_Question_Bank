# Write a Python program to remove duplicate dictionary from a given list.
# Original list with duplicate dictionary: [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
# After removing duplicate dictionary of the said list: [{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

n= int(input("Please enter how many dictionaries you want to enter: "))
print("-"*60)
lst= []
for i in range(n):
    d= {}
    key= input("Please enter your key: ")
    value= input("Please enter your value: ")
    print("-" * 60)
    d[key]= value
    lst.append(d)

olst= []
for val in lst:
    if val not in olst:
        olst.append(val)
print("Original list with duplicate dictionary: ", lst)
print("After removing duplicate dictionary of the said list: ", olst)