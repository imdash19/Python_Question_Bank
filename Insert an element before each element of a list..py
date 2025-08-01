#Write a PYTHON program to insert an element before each element of a list.

lst = [val for val in input("Please enter your elements using space: ").split()]
print("-"*50)

print(("Existing elements: "), lst)
print("-"*50)

uele = [val for val in input("Please enter your elements you want to enter before each existing element: ").split()]
print("-"*50)

print("Extra elements: ", uele)
print("-"*50)

if(len(lst) != len(uele)):
    print("The number of elements to insert must match the number of existing elements.")

else:
    ulst = []
    for before, after in zip(uele, lst):
        ulst.append(before)
        ulst.append(after)

        print("Updated list: ", ulst)
        print("-"*50)
        
print("Program executed successfully")