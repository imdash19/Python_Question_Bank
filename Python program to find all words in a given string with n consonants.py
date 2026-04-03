# Write a Python program to find all words in a given string with n consonants.
# Input: this is our time
# Output:
# Number of consonants: 3
# Words in the said string with 3 consonants:
# ['this']
# Number of consonants: 2
# Words in the said string with 2 consonants:
# ['time']
# Number of consonants: 1
# Words in the said string with 1 consonants:
# ['is', 'our']

s = input().lower()
words = s.split()

vowels = "aeiou"
consonant_map = {}

for word in words:
    count = 0
    for ch in word:
        if ch.isalpha() and ch not in vowels:
            count += 1
    if count not in consonant_map:
        consonant_map[count] = []
    consonant_map[count].append(word)

for key in sorted(consonant_map.keys(), reverse=True):
    print(f"Number of consonants: {key}")
    print(f"Words in the said string with {key} consonants:")
    print(consonant_map[key])