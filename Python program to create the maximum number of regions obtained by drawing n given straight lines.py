# If you draw a straight line on a plane, the plane is divided into two regions. For example, if you draw two straight lines in parallel, you get three areas, and if you draw vertically one to the other you get 4 areas.
# Write a Python program to create the maximum number of regions obtained by drawing n given straight lines.
# Input:
# (1 <= n <= 10,000)
# Input number of straight lines (o to exit):
# 5
# Number of regions:
# 16

while True:
    n = int(input("Input number of straight lines (0 to exit):\n"))
    if n == 0:
        break
    regions = n * (n + 1) // 2 + 1
    print("Number of regions:")
    print(regions)