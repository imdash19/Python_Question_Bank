# Write a Python program to find the two closest distinct numbers in a given list of numbers.
# Input: [1.3, 5.24, 0.89, 21.0, 5.27, 1.3]
# Output: [5.24, 5.27]
# Input: [12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]
# Output: [14.99, 15.0]

lst= [float(val) for val in input().split(', ')]
lst= list(set(lst))
temp= lst[0]
olst= []

for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):

        if abs(lst[i]-lst[j]) < temp:
            
            olst= []
            temp= abs(lst[i]-lst[j])
            olst.append(lst[i])
            olst.append(lst[j])

print(olst)