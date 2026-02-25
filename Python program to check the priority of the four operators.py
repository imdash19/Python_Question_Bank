# Write a Python program to check the priority of the four operators (+, -, *, /).

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

op = input("Enter an operator (+, -, *, /): ")

if op in precedence:
    print(f"Priority of '{op}' is:", precedence[op])

    if precedence[op] == 2:
        print(f"'{op}' has HIGHER precedence.")
    else:
        print(f"'{op}' has LOWER precedence.")
else:
    print("Invalid operator entered.")