"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""
rows=15
l=[]
for i in range(rows):
    a=input()
    a=a.split(' ')
    a=[int(x) for x in a]
    l.append(a)

print(l)

sum=0
maxi=0
for i in reversed(range((rows-1))):
    for j in range(i+1):
        l[i][j] = l[i][j] + max(l[i+1][j],l[i+1][j+1])
        print(i,j)
print(l[0][0])
