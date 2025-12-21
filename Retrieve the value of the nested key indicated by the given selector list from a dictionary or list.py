# Write a Python program to retrieve the value of the nested key
# indicated by the given selector list from a dictionary or list.
# Sample Output: Harwood
#                2

def retrieve_nested_value(data, selector):
    val = data
    for key in selector:
        val = val[key]
    return val


try:
    data = {
        "people": [
            {"name": "John", "city": "New York"},
            {"name": "Alice", "city": "Harwood"}
        ],
        "count": [0, 1, 2]
    }

    selector1 = ["people", 1, "city"]
    selector2 = ["count", 2]

except Exception:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Output:
{retrieve_nested_value(data, selector1)}
{retrieve_nested_value(data, selector2)}''')