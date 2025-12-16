# Write a Python program to join adjacent members of a given list.
# Original list: ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list: ['12', '34', '56', '78']
# Original list: ['1', '2', '3']
# Join adjacent members of a given list: ['12']

def join_adjacent_members_list(lst):
    olst= []
    for i in range(1, len(lst), 2):
        val= lst[i-1] + lst[i]
        olst.append(val)
    return olst

try:
    lst= [val for val in input('Please enter your list values separated with space: ').split()]
    print('='*60)

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst}
 Join adjacent members of a given list: {join_adjacent_members_list(lst)}''')