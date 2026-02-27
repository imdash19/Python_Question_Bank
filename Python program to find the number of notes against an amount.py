# Write a Python program to find the number of notes (Samples of notes: 10, 20, 50, 100, 200, 500) against an amount.
# Range - Number of notes(n): n (1 <= n <= 1000000).

def find_number_of_notes():
    notes= [500, 200, 100, 50, 20, 10]
    print('='*60)
    amount= int(input("Enter the amount: "))
    print('='*60)

    if amount >= 1 and amount <= 1000000:
        nos= {}
        for val in notes:
            if amount >= val:
                no= amount // val
                nos[val]= no
                amount %= val
            else:
                nos[val]= 0
        for no, val in nos.items():
            print(f'{no} ==> {val}')

    else:
        print("Please enter a number between 1 and 100000")
        find_number_of_notes()

find_number_of_notes()