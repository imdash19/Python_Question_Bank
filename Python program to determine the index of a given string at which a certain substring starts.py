# Write a Python program to determine the index of a given string at which a certain substring starts. If the substring is not found in the given string return 'Not found'.

def find_substring(s, sub):
    n = len(s)
    m = len(sub)

    for i in range(n - m + 1):
        if s[i:i + m] == sub:
            return i

    return "Not found"

s = input()
sub = input()

print(find_substring(s, sub))