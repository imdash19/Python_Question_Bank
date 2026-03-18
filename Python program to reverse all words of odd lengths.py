# Write a Python program to reverse all words of odd lengths.
# Sample Input:
# ("The quick brown fox jumps over the lazy dog")
# ("Python Exercises")
# Sample Output:
# The quick brown fox jumps revo the yzal dog
# nohtyP Exercises

sentence = input().strip('()"')

words = sentence.split()

result = []

for word in words:
    if len(word) % 2 != 0:
        result.append(word[::-1])
    else:
        result.append(word)

print(' '.join(result))