#Write a PYTHON program to check if a nested list is a subset of another nested list.
		# Original list: [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
		# Sub list: [[1, 3], [13, 15, 17]]
		# If the one of the said lists is a subset of another: True
		# Original list: [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
		# Sub list: [[[3, 4], [5, 6]]]
		# If the one of the said lists is a subset of another: True
		# Original list: [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
		# Sub list: [[[3, 4], [5, 6]]]
		# If the one of the said lists is a subset of another: False

class InvalidInput(Exception): pass

while True:
    try:
        lst1 = []
        lst2 = []
        n = int(input("Please enter how many inner list you want in list1: "))
        print("-"*70)
        m = int(input("Please enter how many inner list you want in list2: "))
        print("-"*70)
        result = ""

        if(n <= 0 or m <= 0):
            raise InvalidInput

        for i in range(1, n+1):
            print("Inside {} inner list of list1: ".format(i))
            print("~" * 70)
            slst = [val for val in input("Please enter your values separated with space: ").split()]
            print("-" * 70)
            lst1.append(slst)

        for j in range(1, m+1):
            print("Inside {} inner list of list2: ".format(j))
            print("~" * 70)
            slst = [val for val in input("Please enter your values separated with space: ").split()]
            print("-" * 70)
            lst2.append(slst)

        for ele in lst2:
            if(ele in lst1):
                result = True

            else:
                result = False
                break

    except InvalidInput:
        print("-" * 70)
        print("Please don't enter 0 or -VE number.")
        print("-" * 70)

    except ValueError as v:
        print("-" * 70)
        print("Please enter a number (characters, alphanumerics, special symbols aren't allowed): ", v)
        print("-" * 70)

    except Exception as e:
        print("-" * 70)
        print("Something went wrong! Please check again.", e)
        print("-" * 70)

    else:
        print("Original list: {} \n {}".format(lst1, lst2))
        print("-" * 70)
        print("List1 is a subset of List2: ", result)
        break
        print("-" * 70)

    finally:
        print("Program executed successfully")