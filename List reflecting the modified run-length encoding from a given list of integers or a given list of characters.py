# Write a PYTHON program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters.
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	List reflecting the modified run-length encoding from the said list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Original String:
# 	aabcddddadnss
# 	List reflecting the modified run-length encoding from the said string:
# 	[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

try:
    lst = [ele for ele in input("Please enter your string: ").strip()]
    print("-" * 70)
    elst = []

    cnt = 1
    for i in range(0, len(lst)):
        if((i < len(lst)-1) and (lst[i] == lst[i+1])):
            cnt += 1

        else:
            if (cnt > 1):
                elst.append([cnt, lst[i]])
            else:
                elst.append(lst[i])
            cnt = 1

except Exception as e:
    print("-"*70)
    print("Something went wrong! Please try again.", e)
    print("-" * 70)

else:
    print(elst)
    print("-" * 70)

finally:
    print("Program executed successfully.")