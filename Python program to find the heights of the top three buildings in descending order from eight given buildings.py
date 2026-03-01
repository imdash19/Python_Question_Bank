# Write a Python program to find the heights of the top three buildings in descending order from eight given buildings.
# Input:
# 0 <= height of building (integer) <= 10,000
# Input the heights of eight buildings:
# 25
# 35
# 15
# 16
# 30
# 45
# 37
# 39
# Heights of the top three buildings:
# 45
# 39
# 37

heights = []
for _ in range(8):
    heights.append(int(input()))

heights.sort(reverse=True)

print("Heights of the top three buildings:")
for i in range(3):
    print(heights[i])