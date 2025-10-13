# Write a Python program to compute average of two given lists.
# Original list: [1, 1, 3, 4, 4, 5, 6, 7]
#                [0, 1, 2, 3, 4, 4, 5, 7, 8]
# Average of two lists: 3.823529411764706

def average():
    lst1= [int(val) for val in input("Please enter your value of list1 separated by space: ").split()]
    print('-'*60)
    lst2= [int(val) for val in input("Please enter your value of list2 separated by space: ").split()]
    print('-'*60)
    clst= lst1 + lst2
    print("Original list: {} \n{}".format(lst1, lst2))
    print("Average of two lists: ", sum(clst) / len(clst))

average()