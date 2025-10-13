# Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
# 	Original list: [1, 1, 3, 4, 4, 5, 6, 7]
# 	Extract 2 number of elements from the said list which follows each other continuously: [1, 4]
# 	Original lists: [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# 	Extract 4 number of elements from the said list which follows each other continuously: [4]

def continuous_follow():
    lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
    print('-'*60)
    n= 0
    olst= []
    for val in lst:
        if lst[n] == lst[n-1]:
            if val not in olst:
                olst.append(val)
        n += 1
    print("Original list: ", lst)
    print("Extracted {} number of elements from the said list which follows each other continuously: {}".format(len(olst), olst))

continuous_follow()