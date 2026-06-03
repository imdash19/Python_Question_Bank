# Reads a sequence of boolean values (as strings "true"/"false" or "0"/"1") and converts them into a list of actual boolean values (True/False).

values = input().split()

boolean_list = []

for value in values:
    if value.lower() in ("true", "1"):
        boolean_list.append(True)
    elif value.lower() in ("false", "0"):
        boolean_list.append(False)

print(boolean_list)