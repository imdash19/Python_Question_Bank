# 	Write a Python program to create a given flat list of all the keys in a flat dictionary.
# Original directory elements: {'Laura': 10, 'Spencer': 11, 'Bridget': 9, 'Howard ': 10}
# Flat list of all the keys of the said dictionary: ['Laura', 'Spencer', 'Bridget', 'Howard ']

def flat_all_keys(dct):
    lst= []
    for k, v in dct.items():
        lst.append(k)
    return lst

dct= {}
n= int(input('Please enter how many key, value pair you want in the dictionary: '))
print('='*60)

for i in range(n):
    k= input('Please enter your key: ')
    v= input('Please enter your value: ')
    dct[k]= v
    print('='*60)

print(f'''Original directory elements: {dct}
Flat list of all the keys of the said dictionary: {flat_all_keys(dct)}
''')