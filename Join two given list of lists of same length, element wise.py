# Write a Python program to join two given list of lists of same length, element wise.
# Original lists: [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# Join the said two lists element wise: [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
# Original lists: [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# Join the said two lists element wise: [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]

try:
    n= int(input("Please enter how many inner list you want in each list: "))
    if n <= 0:
        raise ValueError

    lst1= []
    lst2= []
    for i in range(n):
        print("=" * 60)
        print(f"Inside {i+1} inner list of first list")
        print("=" * 60)
        slst1= [val for val in input("Please enter your values for list1 separated with space: ").split()]
        lst1.append(slst1)
    for i in range(n):
        print("=" * 60)
        print(f"Inside {i+1} inner list of second list")
        print("=" * 60)
        slst2= [val for val in input("Please enter your values for list2 separated with space: ").split()]
        lst2.append(slst2)

    lst= []
    for a, b in zip(lst1, lst2):
        lst.append(a + b)

except ValueError:
    print("Please don't enter ZERO / NEGATIVE NUMBER / ALPHABET / SPECIAL CHARACTER as input...")

except Exception:
    print("Something went wrong! Please try again later...")

else:
    print(f"""Original lists: {lst1} \n {lst2}
Join the said two lists element wise: {lst}""")