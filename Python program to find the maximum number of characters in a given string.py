# Write a Python program to find the maximum number of characters in a given string.

s = input()

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

max_char = max(freq, key=freq.get)
print(max_char, freq[max_char])