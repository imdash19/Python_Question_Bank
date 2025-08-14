# Write a PYTHON program to count the number of sub lists contain a particular element.
# 		Original list: [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# 		Count 1 in the said list: 3
# 		Count 7 in the said list: 2
# 		Original list: [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# 		Count 'A' in the said list: 3
# 		Count 'E' in the said list: 1

class InvalidInputError(Exception): pass
class SpaceError(Exception): pass

while True:
    try:
        ch = ''
        cnt = 0
        lst = []
        elst = []

        n = int(input("Please enter how many inner list you want: "))
        print("-"*70)

        if(n <= 0):
            raise InvalidInputError

        else:
            for i in range(1, n+1):
                print("Inside {} list".format(i))
                print("-" * 70)
                slst = [ele for ele in input("Please enter a your list elements separated with space: ").split()]
                print("-" * 70)
                lst.append(slst)

                for ele in slst:
                    elst.append(ele)

            ch = input("Please enter your input for counting from list: ")
            print("-" * 70)

            if(len(ch) == 0 or ch.isspace()):
                raise SpaceError

            else:
                cnt = elst.count(ch)


    except InvalidInputError:
        print("Please don't enter O or -VE number")
        print("-" * 70)

    except SpaceError:
        print("Don,t enter space for input")
        print("-" * 70)

    except ValueError as v:
        print("-" * 70)
        print("Please enter a number (characters, alphanumerics, special symbols aren't allowed.): ", v)
        print("-" * 70)

    except Exception as e:
        print("-" * 70)
        print("Something went wrong! Please check again.", e)
        print("-" * 70)

    else:
        print(lst)
        print("-" * 70)
        print("Count '{}' in the said list: {}".format(ch, cnt))
        print("-" * 70)
        break

    finally:
        print("Program executed successfully.")
        print("-" * 70)