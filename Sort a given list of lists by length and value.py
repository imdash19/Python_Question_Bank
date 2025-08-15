#   Write a PYTHON program to sort a given list of lists by length and value.
#   Original list:  [[13, 15, 17], [0], [5, 7], [0, 3], [1, 5], [2, 0]]

#   Sort the list of lists by length and value:  [[0], [0, 3], [1, 5], [2, 0], [5, 7], [13, 15, 17]]

class ZeroNegativeError(Exception):
    pass

while True:
    try:
        lst = []
        n = int(input("Please enter how many sub lists you want: "))
        print("-"*70)

        if(n <= 0):
            raise ZeroNegativeError

        else:
            for i in range(1, n+1):
                print("Inside {} sub list.".format(i))
                print("-" * 70)
                slst = [int(val) for val in input("Please enter your elements separated with space: ").split()]
                print("-" * 70)
                lst.append(slst)

            sortedlst = sorted(lst, key=lambda x: (len(x), x))

    except ZeroNegativeError:
        print("Please don't enter ZERO or NEGATIVE NUMBER for input. Try again.")
        print("-" * 70)

    except ValueError as v:
        print("-" * 70)
        print("Please don't enter ALPHABETS, ALPHANUMERICS, SPECIAL SYMBOLS for input. Try again. ", v)
        print("-" * 70)

    except Exception as e:
        print("-" * 70)
        print("Something went wrong! Check again.", e)
        print("-" * 70)

    else:
        print("Original list: ", lst)
        print("-" * 70)
        print("Sort the list of lists by length and value: ", sortedlst)
        print("-" * 70)
        break

    finally:
        print("Program executed successfully.")
        print("-" * 70)