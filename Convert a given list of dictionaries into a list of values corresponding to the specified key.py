# 	Write a Python program to convert a given list of dictionaries into a list of values corresponding to the specified key.
# Sample Output: [8, 36, 34, 10]

n = int(input("Enter number of dictionaries: "))
lst = []

for i in range(n):
    d = {}
    k = int(input("Enter number of key-value pairs: "))
    for _ in range(k):
        key = input("Key: ")
        value = int(input("Value: "))
        d[key] = value
    lst.append(d)

search_key = input("Enter key to extract values: ")

result = [d[search_key] for d in lst if search_key in d]

print(result)