# Write a Python program to get all possible two-digit letter combinations from a 1-9 digits string.
string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}

digits = input("Enter digits from 1-9 without space: ")

if len(digits) != 2:
    print("Please enter exactly two digits.")
else:
    first_digit, second_digit = digits[0], digits[1]

    if first_digit not in string_maps or second_digit not in string_maps:
        print("Invalid digit entered. Only digits 1-9 allowed.")
    else:
        combinations = []

        for ch1 in string_maps[first_digit]:
            for ch2 in string_maps[second_digit]:
                combinations.append(ch1 + ch2)

        print("\nAll possible two-digit letter combinations:\n")
        for combo in combinations:
            print(combo)

        print("\nTotal combinations:", len(combinations))