# Write a Python program to remove duplicate words from a given list of strings.
# Original String: ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
# After removing duplicate words from the said list of strings: ['Python', 'Exercises', 'Practice', 'Solution']

lst= [val for val in input("Please enter your values separated with space: ").split()]
print("="*60)
olst= []
for i in lst:
    if i not in olst:
        olst.append(i)
print(f"""Original String: {lst}
After removing duplicate words from the said list of strings: {olst}""")