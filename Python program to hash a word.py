# Write a Python program to hash a word

import hashlib

def hash_word():
    word = input("Enter a word to hash: ")

    hashed_word = hashlib.sha256(word.encode()).hexdigest()

    print("\nOriginal word:", word)
    print("SHA-256 Hash:", hashed_word)

hash_word()