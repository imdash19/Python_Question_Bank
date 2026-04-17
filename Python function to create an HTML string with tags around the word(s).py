# Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result:
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def add_tags(tag, text):
    return f"<{tag}>{text}</{tag}>"

tag = input()
text = input()

print(add_tags(tag, text))