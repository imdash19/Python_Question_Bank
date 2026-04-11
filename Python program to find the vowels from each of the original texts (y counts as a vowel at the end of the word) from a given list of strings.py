# Write a Python program to find the vowels from each of the original texts (y counts as a vowel at the end of the word) from a given list of strings.
# Input: ['w3resource', 'Python', 'Java', 'C++']
# Output: ['eoue', 'o', 'aa', '']
# Input: ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
# Output: ['ay', 'auy', 'aeeay', 'aaey', 'aoeey']

lst = eval(input())

res = []
vowels = "aeiou"

for word in lst:
    temp = ""
    for i in range(len(word)):
        if word[i].lower() in vowels or (word[i].lower() == 'y' and i == len(word) - 1):
            temp += word[i]
    res.append(temp)

print(res)