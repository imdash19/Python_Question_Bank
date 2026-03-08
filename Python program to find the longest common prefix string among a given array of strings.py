# Write a Python program to find the longest common prefix string among a given array of strings. Return false if there is no common prefix.
# For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
# Sample Input:
# ["abcdefgh","abcefgh"]
# ["w3r","w3resource"]
# ["Python","PHP", "Perl"]
# ["Python","PHP", "Java"]
# Sample Output:
# abc
# w3r
# P

arr=eval(input())
p=arr[0]
for s in arr[1:]:
    while not s.startswith(p):
        p=p[:-1]
        if p=="":
            print(False)
            exit()
print(p)