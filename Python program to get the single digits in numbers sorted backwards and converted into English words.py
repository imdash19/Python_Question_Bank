# Write a Python program to get the single digits in numbers sorted backwards and converted into English words.
# Input: [1, 3, 4, 5, 11]
# Output: ['five', 'four', 'three', 'one']
# Input: [27, 3, 8, 5, 1, 31]
# Output: ['eight', 'five', 'three', 'one']

lst = list(map(int, input().strip('[]').split(',')))

words = ["zero","one","two","three","four","five","six","seven","eight","nine"]

res = sorted(set([x for x in lst if 0 <= x <= 9]), reverse=True)

print([words[x] for x in res])