# Write a Python program to find the name of the oldest student in a given dictionary containing the names and ages of a group of students.
# Sample Input:
# {"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}
# {"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4, "Joannie Archibald": 12.6, "Becki Saunder": 12.7}
# Sample Output:
# Nidia Dominique
# Becki Saunder

d = eval(input())

oldest_name = ""
max_age = -1

for name in d:
    if d[name] > max_age:
        max_age = d[name]
        oldest_name = name

print(oldest_name)