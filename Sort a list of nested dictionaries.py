# Write a PYTHON program to sort a list of nested dictionaries.

my_collection = {'KEY1':{'name':'foo','data':1351,'completed':100}, 'KEY2':{'name':'bar','data':1541,'completed':12}, 'KEY3':{'name':'baz','data':58413,'completed':18}}

sorted_items = sorted(my_collection.items(), key=lambda item: item[1]['name'])

for key, value in sorted_items:
    print(f"{key}: {value}")

print("-"*70)

print("Program executed successfully")