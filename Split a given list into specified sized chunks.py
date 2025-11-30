# Write a Python program to split a given list into specified sized chunks.
# Original list: [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the said list into equal size 3: [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 4: [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 5: [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]

try:
    lst = [int(val) if (val.lstrip("-")).isdigit() else val for val in input("Please enter your values separated with space: ").split()]
    print("=" * 60)
    ch = int(input("Enter your choice to split the said list into equal size: "))
    print("=" * 60)
    if ch <= 0:
        raise ValueError("Chunk size must be positive.")
    slst = []
    for i in range(0, len(lst), ch):
        ilst = lst[i:i + ch]
        slst.append(ilst)

except ValueError:
    print("Please enter a valid positive number. Try again...")

except Exception:
    print("Something went wrong. Try again later...")

else:
    print(f"""Original list: {lst}
Split the said list into equal size {ch}: {slst}""")
