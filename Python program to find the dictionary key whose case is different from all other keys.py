# Write a Python program to find the dictionary key whose case is different from all other keys.
# Input: {'red': '', 'GREEN': '', 'blue': 'orange'}
# Output: GREEN
# Input: {'RED': '', 'GREEN': '', 'orange': '#125GD'}
# Output: orange

n= int(input('Enter how many dictionary elements you want: '))
d= {}

for i in range(n):
    k, v= map(str, input('Enter key & values here: ').split())
    d[k]= v

lc= []
uc= []
mc= []
for v in d.keys():
    if v.isupper():
        uc.append(v)
    elif v.islower():
        lc.append(v)
    else:
        mc.append(v)
        
if len(uc) > len(lc) and len(uc) > len(mc):
    print(*lc)
elif len(lc) > len(uc) and len(lc) > len(mc):
    print(*uc)
else:
    print(*mc)