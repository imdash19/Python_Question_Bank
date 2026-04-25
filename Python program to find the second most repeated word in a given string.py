# Write a Python program to find the second most repeated word in a given string.

text = input()

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

counts = sorted(set(freq.values()), reverse=True)

if len(counts) < 2:
    print("No second most repeated word")
else:
    second_max = counts[1]
    result = [w for w in words if freq[w] == second_max]

    for w in result:
        print(w)
        break