# Write a Python program to find the maximum and minimum values in a given list of tuples.
# Original list with tuples: [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
# Maximum and minimum values of the said list of tuples: (78, 60)

lst= [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
slst= []
for i in lst:
    for j in i:
        if type(j) == int:
            slst.append(int(j))
        else:
            pass
print(f"""Original list with tuples: {lst}
    Maximum and minimum values of the said list of tuples: ({max(slst)}, {min(slst)})""")