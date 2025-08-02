# Write a PYTHON program to convert list to list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

colorlst = [val for val in input("Please enter the color names using space: ").split()]
print("-"*70)
codelst = [val for val in input("Please enter the color names using space: ").split()]
print("-"*70)

if(len(colorlst) != len(codelst)):
    print("Number of color list & color code should be equal.")
    print("-"*70)

else:
    lst = []
    for color, code in zip(colorlst, codelst):
        d = {}
        d["Color Name"] = color
        d["Color Code"] = code
        lst.append(d)

    print(lst)
    print("-"*70)

print("Program executed successfully")