#Write a PYTHON program to split a list based on first character of word.

lst = [word for word in input("Please enter a line of text: ").split()]
print("-"*50)

def split_by_first_char(lst):
    result = {}
    for words in lst:
        first_char = words[0].lower()

        if first_char not in result:
            result[first_char] = []

        result[first_char].append(words)

    return result

print(split_by_first_char(lst))
print("-"*50)

print("Program executed successfully")