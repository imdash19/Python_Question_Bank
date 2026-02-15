# Write a Python program to remove the first item from a specified list.

def remove_first_item():
    user_input = input("Enter list items separated by space: ")
    items = user_input.split()
    print("Original List:", items)
    if items:
        removed_item = items.pop(0)
        print("Removed Item:", removed_item)
        print("Updated List:", items)
    else:
        print("The list is empty. Nothing to remove.")
remove_first_item()