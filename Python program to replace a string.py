# Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string.
# Input: English letters (including single byte alphanumeric characters, blanks, symbols) are given on one line. The length of the input character string is 1000 or less.
# Input a text with two words 'Python' and 'Java'
# Python is popular than Java
# Java is popular than Python

def replace_words():
    try:
        s=input()
        s=s.replace("Python","#")
        s=s.replace("Java","Python")
        s=s.replace("#","Java")
        print(s)
    except:
        pass

replace_words()