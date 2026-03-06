# There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green. Blue represents the sea, and green represents the land. When two green squares are in contact with the top and bottom, or right and left, they are said to be ground. The area created by only one green square is called "island". For example, there are five islands in the figure below.
# Write a Python program to read the mass data and find the number of islands.
# Input:
# Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros
# 1100000111
# 1000000111
# 0000000111
# 0010001000
# 0000011100
# 0000111110
# 0001111111
# 1000111110
# 1100011100
# 1110001000
# Number of islands:
# 5

def dfs(g,i,j):
    if i<0 or i>=10 or j<0 or j>=10 or g[i][j]==0:
        return
    g[i][j]=0
    dfs(g,i+1,j)
    dfs(g,i-1,j)
    dfs(g,i,j+1)
    dfs(g,i,j-1)

g=[]
for _ in range(10):
    g.append(list(map(int,list(input().strip()))))

c=0
for i in range(10):
    for j in range(10):
        if g[i][j]==1:
            c+=1
            dfs(g,i,j)

print("Number of islands:")
print(c)