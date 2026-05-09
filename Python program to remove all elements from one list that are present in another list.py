# Write a Python program to remove all elements from one list that are present in another list.
# The program should accept two space-separated lists from the user.
# Remove elements from the first list that appear in the second list.
# Use list comprehension and the not in operator.
# Display the filtered list as output.

lst1= list(map(int, input().split()))
lst2= list(map(int, input().split()))

for val in lst2:
    if val in lst1:
        lst1.remove(val)

print(lst1)
