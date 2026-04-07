# Write a Python program to find the sum of the even elements that are at odd indices in a given list.
# Input: [1, 2, 3, 4, 5, 6, 7]
# Output: 12
# Input: [1, 2, 8, 3, 9, 4]
# Output: 6

lst= list(map(int, input().split()))
sum= 0
for i in range(1, len(lst), 2):
    if lst[i]% 2 == 0:
        sum+= lst[i]

print(sum)