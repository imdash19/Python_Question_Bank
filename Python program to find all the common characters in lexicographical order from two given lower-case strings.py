# Write a Python program to find all the common characters in lexicographical order from two given lower-case strings. If there are no similar letters print "No common characters".

s1 = input().strip()
s2 = input().strip()

common = sorted(set(s1) & set(s2))

if common:
    print("".join(common))
else:
    print("No common characters")
