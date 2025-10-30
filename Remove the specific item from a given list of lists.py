# Write a Python program to remove the specific item from a given list of lists.
# Original list of lists:
# Remove 1st list from the saod given list of lists: [['Maroon', 'Yellow', 'Olive'], ['#800000', '#FFFF00', '#808000'], ['rgb (128,0,0)', 'rgb (255,255,0)', 'rgb (128,128,0)']]
# Remove 2nd list from the saod given list of lists: [['Red', 'Yellow', 'Olive'], ['#FF0000', '#FFFF00', '#808000'], ['rgb (255,0,0)', 'rgb (255,255,0)', 'rgb (128,128,0)']]
# Remove 4th list from the saod given list of lists: [['Red', 'Maroon', 'Yellow'], ['#FF0000', '#800000', '#FFFF00'], ['rgb (255,0,0)', 'rgb (128,0,0)', 'rgb (255,255,0)']]

n= int(input("Please enter number of lists you want: "))
lst= []
for i in range(n):
    print("="*60)
    print(f"Inside {i+1} inner list")
    print("="*60)
    slst= [val for val in input("Please enter your value separated by space: ").split()]
    lst.append(slst)

i= int(input("Please enter your index choice for removing item: "))
print("="*60)
print(f"Original list of lists: {lst}")
for val in lst:
    val.pop(i-1)
print(f"Remove {i} list from the saod given list of lists: {lst}")