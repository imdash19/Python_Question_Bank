# Write a Python program that reads text (only alphabetical characters and spaces) and prints two words. The first word is the one that appears most often in the text. The second one is the word with the most letters.
# Note: A word is a sequence of letters which is separated by the spaces.
#
# Input:
# A text is given in a line with following condition:
# a. The number of letters in the text is less than or equal to 1000.
# b. The number of letters in a word is less than or equal to 32.
# c. There is only one word which is arise most frequently in given text.
# d. There is only one word which has the maximum number of letters in given text.
# Input text: Thank you for your comment and your participation.
# Output: your participation.

def find_words():
    try:
        t=input()
        t=t.replace('.','')
        w=t.split()
        c={}
        for i in w:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        a=''
        b=0
        for i in c:
            if c[i]>b:
                b=c[i]
                a=i
        d=''
        for i in w:
            if len(i)>len(d):
                d=i
        print(a,d)
    except:
        pass

find_words()