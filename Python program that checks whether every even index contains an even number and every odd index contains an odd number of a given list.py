# Write a Python program that checks whether every even index contains an even number and every odd index contains an odd number of a given list.
# Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 3]
# Check whether every even index contains an even number and every
# odd index contains odd number of a given list:
# True
# Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 4]
# Check whether every even index contains an even number and every
# odd index contains odd number of a given list:
# False
# Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 4]
# Check whether every even index contains an even number and every
# odd index contains odd number of a given list:
# True

lst=eval(input())
flag=True
for i in range(len(lst)):
    if i%2==0 and lst[i]%2!=0:
        flag=False
    if i%2==1 and lst[i]%2!=1:
        flag=False
print(flag)