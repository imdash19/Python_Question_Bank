# Program to print long text, convert it into a list, and print all words with their frequency

def word_frequency():
    print("Enter your long text below:")
    text = input("> ")
    print("\n" + "="*60)
    text = text.lower()

    for ch in [",", ".", "!", "?", ":", ";", '"', "'"]:
        text = text.replace(ch, "")

    words = text.split()

    print("\nList of Words:")
    print(words)

    print("\n" + "="*60)
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("\nWord Frequency:\n")
    for word, count in frequency.items():
        print(f"{word} : {count}")

word_frequency()