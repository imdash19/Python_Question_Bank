# Write a PYTHON program to sort each sub list of strings in a given list of lists.
# 	Original list: [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# 	Sort the list of lists by length and value: [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

class ZeroNegativeError(Exception):
    pass

while True:
    try:
        lst = []
        n = int(input("Please enter how many sub lists you want: "))
        print("-" * 70)
    
        if n <= 0:
            raise ZeroNegativeError
    
        for i in range(1, n+1):
            print('Inside {} sub list.'.format(i))
            print("-" * 70)
            slst = list(map(int, input("Please enter your sub list elements: ").split()))
            print("-" * 70)
            lst.append(slst)
    
        for sub in lst:
            sub.sort()
    
        sortedlst = sorted(lst, key=lambda x: (len(x), x))
    
    except ZeroNegativeError:
        print("Please don't enter ZERO or NEGATIVE number for input. Try again.")
        print("-" * 70)
    
    except ValueError as v:
        print("-"*70)
        print("Don't enter ALPHABETS, ALPHANUMERICS, SPECIAL SYMBOLS for input. Try again.", v)
        print("-" * 70)
    
    except Exception as e:
        print("-" * 70)
        print("Something went wrong! Please check again.", e)
        print("-" * 70)
    
    else:
        print("Original list: ", lst)
        print("-" * 70)
        print("Sorted list: ", sortedlst)
        print("-" * 70)
        break
    
    finally:
        print("Program executed successfully.")

    print("-" * 70)
