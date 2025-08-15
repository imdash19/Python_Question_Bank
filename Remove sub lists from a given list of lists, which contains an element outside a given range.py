#   Write a PYTHON program to remove sub lists from a given list of lists, which contains an element outside a given range.
# 	Original list: [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# 	After removing sub lists from a given list of lists, which contains an element outside the given range: [[13, 14, 15, 17]]

class ZeroNegativeError(Exception):
    pass

    while True:
    try:
        lst = []
        result = []
        n = int(input("Please enter how many sub lists you want: "))
        print("-"*70)
    
        if(n <= 0):
            raise ZeroNegativeError
    
        else:
            for i in range(1, n+1):
                print("Inside {} list.".format(i))
                print("-" * 70)
                slst = [int(val) for val in input("Please enter your elements separate with space: ").split()]
                print("-" * 70)
                lst.append(slst)
    
            start = int(input("Please enter your starting index: "))
            print("-" * 70)
            end = int(input("Please enter your ending index: "))
            print("-" * 70)
    
            for sele in lst:
                for val in sele:
                    if(val not in range(start, end+1)):
                        break
                else:
                    print(sele)
                    result.append(sele)
    
    except ZeroNegativeError:
        print("Please don't enter ZERO or NEGATIVE number for input. Try again.")
        print("-" * 70)
    
    except ValueError as v:
        print("-" * 70)
        print("Please don't enter ALPHABETS, ALPHANUMERICS, SPECIAL SYMBOLS for input. Try again.", v)
        print("-" * 70)
    
    except Exception as e:
        print("-" * 70)
        print("Something went wrong! Check again.", e)
        print("-" * 70)
    
    else:
        print("Original list: ", lst)
        print("-" * 70)
        print("After removing sub lists from a given list of lists, which contains an element outside the given range: ", result)
        print("-" * 70)
        break
    
    finally:
        print("Program executed successfully.")

    print("-" * 70)
