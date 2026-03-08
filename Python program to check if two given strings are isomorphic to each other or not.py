# In abstract algebra, a group isomorphism is a function between two groups that sets up a one-to-one correspondence between the elements of the groups in a way that respects the given group operations. If there exists an isomorphism between two groups, then the groups are called isomorphic.
# Two strings are isomorphic if the characters in string A can be replaced to get string B
# Given "foo", "bar", return false.
# Given "paper", "title", return true.
# Write a Python program to check if two given strings are isomorphic to each other or not.
# Sample Input:
# ("foo", "bar")
# ("bar", "foo")
# ("paper", "title")
# ("title", "paper")
# ("apple", "orange")
# ("aa", "ab")
# ("ab", "aa")
# Sample Output:
# False
# False
# True
# True
# False
# False
# False

a,b=eval(input())
if len(a)!=len(b):
    print(False)
else:
    m1={}
    m2={}
    f=True
    for i in range(len(a)):
        if a[i] in m1 and m1[a[i]]!=b[i]:
            f=False
            break
        if b[i] in m2 and m2[b[i]]!=a[i]:
            f=False
            break
        m1[a[i]]=b[i]
        m2[b[i]]=a[i]
    print(f)