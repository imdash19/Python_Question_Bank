# Write a Python program to create a sequence where the first four members of the sequence are equal to one. Each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence.

def find_nth_term():
    n = int(input("Enter the value of N: "))

    if n <= 0:
        print("Please enter a positive integer.")
        return

    sequence = [1, 1, 1, 1]

    if n <= 4:
        print(f"{n}th term of the sequence is: 1")
        return

    for i in range(4, n):
        next_term = (
            sequence[i-1] +
            sequence[i-2] +
            sequence[i-3] +
            sequence[i-4]
        )
        sequence.append(next_term)

    print(f"{n}th term of the sequence is: {sequence[n-1]}")

find_nth_term()