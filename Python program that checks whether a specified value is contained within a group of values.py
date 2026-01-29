# 	Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data:
# 3 -> [1, 5, 8, 3]: True
# -1 -> [1, 5, 8, 3]: False

def is_value_in_group(value, group):
    return value in group

value = int(input("Enter the value to search: "))

group_input = input("Enter the group of values (comma-separated): ")
group = list(map(int, group_input.split(',')))

print('=' * 50)

result = is_value_in_group(value, group)
print(result)