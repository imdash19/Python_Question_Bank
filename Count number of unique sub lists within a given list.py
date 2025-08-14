# Write a PYTHON program to count number of unique sub lists within a given list.
# 	Original list: [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# 	Number of unique lists of the said list: {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
# 	Original list: [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
# 	Number of unique lists of the said list: {('green', 'orange'): 2, ('black',): 1, ('white',): 1}

class ZeroNegativeError(Exception):pass
class SpaceError(Exception): pass

while True:
    try :
        lst = []
        d = {}
        n = int(input("Please enter how many sub lists you want: "))
        print("-"*70)

        if(n <= 0):
            raise ZeroNegativeError

        else:
            for i in range(1, n+1):
                print("Inside {} sub list.".format(i))
                print("-" * 70)
                slst = [ele.lower() for ele in input("Please enter your list elements separated with space: ").split()]
                print("-" * 70)
                lst.append(slst)

            for sele in lst:
                cnt = lst.count(sele)
                d[tuple(sele)] = cnt

    except ZeroNegativeError:
        print("Don't enter ZERO or -VE number as input. Try again.")
        print("-" * 70)

    except SpaceError:
        print("Don't enter SPACE for input. Try again.")
        print("-" * 70)

    except ValueError as v:
        print("-" * 70)
        print("Don't enter ALPHABETS, ALPHANUMERICS, SPECIAL SYMBOLS for input. Try again.", v)
        print("-" * 70)

    except Exception as e:
        print("-" * 70)
        print("Something went wrong! Please check again.", e)
        print("-" * 70)

    else:
        print("Original list: ", lst)
        print("-" * 70)
        print("Number of unique lists of the said list: ", d)
        print("-" * 70)
        break

    finally:
        print("Program executed successfully")