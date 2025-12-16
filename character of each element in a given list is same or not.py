#  Write a Python program to check if first digit/character of each element in a given list is same or not.
# Original list: [1234, 122, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not! True
# Original list: [1234, 922, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not! False
# Original list: ['aabc', 'abc', 'ab', 'a']
# Check if first character in each element of the said given list is same or not! True
# Original list: ['aabc', 'abc', 'ab', 'ha']
# Check if first character in each element of the said given list is same or not! False

def check_first_digit_or_character_same_or_not(lst):
    result= False
    fe= str(lst[0])[0]
    for val in lst:
        if val[0] == fe:
            result = True
        else:
            result = False
            break
    return result

try:
    lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your list elements separated with space: ').split()]
    print('='*60)

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst}
 Check if first character in each element of the said given list is same or not! {check_first_digit_or_character_same_or_not(lst)}''')