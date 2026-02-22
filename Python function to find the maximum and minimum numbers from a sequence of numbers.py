def find_max_min():
    lst = [int(val) for val in input(
        "Please enter your sequence of numbers separated with space: "
    ).split()]

    print("=" * 60)

    if not lst:
        print("No numbers entered.")
        return

    maxi = lst[0]
    mini = lst[0]

    for val in lst:
        if val > maxi:
            maxi = val
        if val < mini:
            mini = val

    print("The maximum number is:", maxi)
    print("The minimum number is:", mini)

find_max_min()