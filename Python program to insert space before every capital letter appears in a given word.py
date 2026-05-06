# Write a Python program to insert space before every capital letter appears in a given word.
# Sample Data:
# ("PythonExercises") -> "Python Exercises"
# ("Python") -> "Python"
# ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"

text = input()

result = text[0]

for i in range(1, len(text)):
    if text[i].isupper():
        result += " "
    result += text[i]

print(result)