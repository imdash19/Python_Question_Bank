# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String: 'abc', 'xyz'
# Expected Result: 'xyc abz'

s1, s2= input().split(',')
ns= s2[:2]+s1[2:]+' '+s1[:2]+s2[2:]
print(ns)