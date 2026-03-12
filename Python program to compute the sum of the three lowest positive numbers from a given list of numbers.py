# Write a Python program to compute the sum of the three lowest positive numbers from a given list of numbers.
# Original list of numbers: [10, 20, 30, 40, 50, 60, 7]
# Sum of the three lowest positive numbers of the said array: 37
# Original list of numbers: [1, 2, 3, 4, 5]
# Sum of the three lowest positive numbers of the said array: 6
# Original list of numbers: [0, 1, 2, 3, 4, 5]
# Sum of the three lowest positive numbers of the said array: 6

lst=list(map(int,input("Enter numbers separated by space: ").split()))

lst=[i for i in lst if i>0]
lst.sort()

print(lst[0]+lst[1]+lst[2])