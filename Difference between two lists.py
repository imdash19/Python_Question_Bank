#Write a PYTHON program to compute the difference between two lists.
# Sample data: [red orange green blue white], [black yellow green blue]
# Expected Output:
# 	Color1-Color2: ['white', 'orange', 'red']
# 	Color2-Color1: ['black', 'yellow']

clst1 = [name for name in input("Please enter the color names for list1 with space: ").split()]
print("-"*70)
clst2 = [name for name in input("Please enter the color names for list2 with space: ").split()]
print("-"*70)

if(len(clst1) == 0 and len(clst2) == 0):
    print("Please enter a valid input")
    print("-" * 70)

else:
    rclst1 = [color for color in clst1 if color not in clst2]
    rclst2 = [color for color in clst2 if color not in clst1]

    print("Color1 - Color2: ", rclst1)
    print("-" * 70)
    print("Color2 - Color1: ", rclst2)
    print("-" * 70)

print("Program executed successfully")