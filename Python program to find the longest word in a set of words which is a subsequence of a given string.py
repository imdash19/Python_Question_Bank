# In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, the sequence (A, B, D) is a subsequence of (A, B, C, D, E, F) obtained after removal of elements C, E, and F. The relation of one sequence being the subsequence of another is a preorder.
# The subsequence should not be confused with substring (A, B, C, D) which can be derived from the above string (A, B, C, D, E, F) by deleting substring (E, F). The substring is a refinement of the subsequence.
# The list of all subsequences for the word "apple" would be "a", "ap", "al", "ae", "app", "apl", "ape", "ale", "appl", "appe", "aple", "apple", "p", "pp", "pl", "pe", "ppl", "ppe", "ple", "pple", "l", "le", "e", "".
# Write a Python program to find the longest word in a set of words which is a subsequence of a given string.
# Sample Input:
# ("Green", {"Gn", "Gren", "ree", "en"})
# ("pythonexercises", {"py", "ex", "exercises"})
# Sample Output:
# Gren
# Exercises

import sys

def is_subsequence(s, w):
    i = 0
    for c in s:
        if i < len(w) and c == w[i]:
            i += 1
    return i == len(w)

try:
    while True:
        s, words = eval(input())
        s = s.lower()
        best = ""
        for w in words:
            wl = w.lower()
            if is_subsequence(s, wl):
                if len(w) > len(best):
                    best = w
        print(best.capitalize())
except EOFError:
    pass