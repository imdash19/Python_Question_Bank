# Write a PYTHON program to find a tuple, the smallest second index value from a list of tuples.

n = int(input("Please enter how many inner tuple you want: "))
print("-"*70)

try:
    if(n <= 0):
        print("Please enter a valid input")
        print("-" * 70)

    else:
        lst = []

        for i in range(1, n+1):
            print("{} tuple".format(i))
            print("-" * 70)

            tlst = [int(val) for val in input("Please enter the tuple elements: ").split()]
            print("-" * 70)
            
            tup = tuple(tlst)
            lst.append(tup)

except ValueError:
    print("Please enter a integer")

except IndexError:
    print("Please enter at-least 2 elements")

else:
    small = min(lst, key = lambda x:x[1])

finally:
    print("Tuple with the smallest second value:", small)