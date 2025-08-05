#Write a PYTHON program to create a list with infinite elements.

def infinite():
    i = 1
    while True:
        yield i
        i += 1

res = infinite()
print(next(res))

for val in res:
    print(val)

print("-"*70)
print("Program executed successfully")