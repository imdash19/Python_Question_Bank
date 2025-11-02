# Write a Python program to compute the sum of digits of each number of a given list.
# Original list: [10, 2, 56]
# Sum of digits of each number of the said list of integers:14
# Original list: [10, 20, 4, 5, 'b', 70, 'a']
# Sum of digits of each number of the said list of integers:19
# Original list: [10, 20, -4, 5, -70]
# Sum of digits of each number of the said list of integers: 19

try:
    lst = input("Please enter your values separated with space: ").split()
    print("="*60)
    slst = []
    for val in lst:
        if val.lstrip('-').isdigit():
            num = abs(int(val))
            for digit in str(num):
                slst.append(int(digit))

except Exception:
    print("Something went wrong! Try again later.")

else:
    print(f"""Original list: {lst}
Sum of digits of each number of the said list of integers: {sum(slst)}""")