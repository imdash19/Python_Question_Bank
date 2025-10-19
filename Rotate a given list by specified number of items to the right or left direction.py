# Write a Python program to rotate a given list by specified number of items to the right or left direction.
# Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Rotate the said list in left direction by 4: [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
# Rotate the said list in left direction by 2: [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# Rotate the said list in Right direction by 4: [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
# Rotate the said list in Right direction by 2: [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

lst= [int(val) for val in input("Please enter values separated with space: ").split()]
rn= int(input("Please enter the number from which you want to rotate: "))
ch= input("Please enter your choice to rotate in which direction left/right (l/r): ")
print('-'*60)
print("Original List: ", lst)
match ch.lower():
    case "l":
        for i in range(rn):
            p= lst.pop(0)
            lst.append(p)
        print(f"Rotate the said list in left direction by {rn}: {lst}")
    case "r":
        for i in range(rn):
            p= lst.pop(-1)
            lst.insert(0, p)
        print(f"Rotate the said list in left direction by {rn}: {lst}")
    case _:
        print("Invalid choice!")