# Write a Python program to test whether a passed letter is a vowel or not.

def check_vowel(letter):
    if letter in 'aeiouAEIOU':
        return True
    else:
        return False

letter= input("Enter a letter: ")
if check_vowel(letter):
    print('It is a vowel')

else:
    print('It is not a vowel')