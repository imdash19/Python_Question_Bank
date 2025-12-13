#  Write a Python program to form Bigrams of words in a given list of strings.
# From Wikipedia: A bigram or diagram is a sequence of two adjacent elements from a string of tokens, which are typically letters, syllables, or words. A bigram is an n-gram for n=2. The frequency distribution of every bigram in a string is commonly used for simple statistical analysis of text in many applications, including in computational linguistics, cryptography, speech recognition, and so on.
# Original list: ['Sum all the items in a list', 'Find the second-smallest number in a list']
# Bigram sequence of the said list: [('Sum', 'all'), ('all', 'the'), ('the', 'items'), ('items', 'in'), ('in', 'a'), ('a', 'list'), ('Find', 'the'), ('the', 'second'), ('second', 'smallest'), ('smallest', 'number'), ('number', 'in'), ('in', 'a'), ('a', 'list')]

def bigram_words(lst):
    olst= []
    for val in lst:
        words = val.split()
        for i in range(len(words) - 1):
            olst.append((words[i], words[i + 1]))
    return olst

try:
    lst= [val for val in input('Please enter your list values separated with comma: ').split(',')]
    print('='*60)

except Exception:
    print('Something went wrong :( Please try again...')

else:
    print(f'''Original list: {lst}
 Bigram sequence of the said list: {bigram_words(lst)}''')