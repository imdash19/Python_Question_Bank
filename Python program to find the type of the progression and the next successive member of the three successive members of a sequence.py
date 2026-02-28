# Write a Python program to find the type of the progression (arithmetic progression / geometric progression) and the next successive member of the three successive members of a sequence.
# According to Wikipedia, an arithmetic progression (AP) is a sequence of numbers such that the difference of any two successive members of the sequence is a constant. For instance, the sequence 3, 5, 7, 9, 11, 13, . . . is an arithmetic progression with common difference 2. For this problem, we will limit ourselves to arithmetic progression whose common difference is a non-zero integer.
# On the other hand, a geometric progression (GP) is a sequence of numbers where each term after the first is found by multiplying the previous one by a fixed non-zero number called the common ratio. For example, the sequence 2, 6, 18, 54, . . . is a geometric progression with common ratio 3. For this problem, we will limit ourselves to geometric progression whose common ratio is a non-zero integer.

def find_progression():
    print("Enter three successive members of the sequence:")
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))

    # Check for Arithmetic Progression
    if (b - a == c - b) and (b - a != 0):
        difference = b - a
        next_term = c + difference
        print("\nIt is an Arithmetic Progression (AP)")
        print("Next successive member:", next_term)

    # Check for Geometric Progression
    elif (a != 0 and b % a == 0 and c % b == 0):
        if (b // a == c // b) and (b // a != 0):
            ratio = b // a
            next_term = c * ratio
            print("\nIt is a Geometric Progression (GP)")
            print("Next successive member:", next_term)
        else:
            print("\nIt is neither AP nor GP")

    else:
        print("\nIt is neither AP nor GP")

find_progression()