# Write a Python program to convert GPAs to letter grades according to the following table:
# GPAs	Grades
# 4.0:	A+
# 3.7:	A
# 3.4:	A-
# 3.0:	B+
# 2.7:	B
# 2.4:	B-
# 2.0:	C+
# 1.7:	C
# 1.4:	C-
# below:	F
# Input: [4.0, 3.5, 3.8]
# Output: ['A+', 'A-', 'A']
# Input: [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
# Output: ['A+', 'A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']

lst= [float(val) for val in input('Enter your GPAs separated with space: ').split(', ')]

olst= []
for val in lst:
    if val >= 4.0:
        olst.append('A+')

    elif val < 4 and val  >= 3.7:
        olst.append('A')

    elif val < 3.7 and val  >= 3.4:
        olst.append('A-')

    elif val < 3.4 and val  >= 3.0:
        olst.append('B+')

    elif val < 3.0 and val  >= 2.7:
        olst.append('B')

    elif val < 2.7 and val >= 2.4:
        olst.append('B-')

    elif val < 2.4 and val  >= 2.0:
        olst.append('C+')

    elif val < 2.0 and val  >= 1.7:
        olst.append('C')

    elif val < 1.7 and val  >= 1.4:
        olst.append('C-')

    else:
        olst.append('F')

print(olst)