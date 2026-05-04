# Write a Python program to replace each character of a word of length five and more with a hash character (#).
# Sample Output:
# Original string: Count the lowercase letters in the said list of words:
# Replace words (length five or more) with hash characters in the said string:
# ##### the ######### ####### in the said list of ######
# Original string: Python - Remove punctuations from a string:
# Replace words (length five or more) with hash characters in the said string:
# ###### - ###### ############ from a #######

text = input("Enter a string:\n")

words = text.split()
result = []

for word in words:
    clean = ''.join(ch for ch in word if ch.isalpha())
    if len(clean) >= 5:
        new_word = ''
        for ch in word:
            if ch.isalpha():
                new_word += '#'
            else:
                new_word += ch
        result.append(new_word)
    else:
        result.append(word)

print("Replace words (length five or more) with hash characters in the said string:")
print(' '.join(result))