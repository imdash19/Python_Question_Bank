# Write a Python program to find the smallest and largest words in a given string.

def find_words(s):
    words = s.split()
    smallest = words[0]
    largest = words[0]

    for word in words:
        if len(word) < len(smallest):
            smallest = word
        if len(word) > len(largest):
            largest = word

    return smallest, largest

s = input()
small, large = find_words(s)
print("Smallest word:", small)
print("Largest word:", large)