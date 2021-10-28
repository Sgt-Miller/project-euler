#up and down are the same for this problem
#same with left and right
#there are two possible diagonal directions
x=20
y=x
ad=4

#make a 2d array
l=[]
for i in range(x):
    a=input().split(' ')
    a=[int(x) for x in a if x != ' ']
    l.append(a)
max=0

p=1
#check left to right
for i in range(x):
    for j in range(x-ad+1):
        for k in range(4):
            p=p*l[i][j+k]          
        if p>max:
            max=p
        p=1
print(max)
#check up to down
for j in range(x):
    for i in range(x-ad+1):
        for k in range(4):
            p=p*l[i+k][j]
        if p>max:
            max=p
        p=1
print(max)
#check forward diagonal
for i in range(x-ad+1):
    for j in range(x-ad+1):
        for k in range(4):
            p=p*l[i+k][j+k]
        if p>max:
            max=p
        p=1
print(max)
#check backward diagonal
for i in range(ad-1,x):
    for j in range(x-ad+1):
        for k in range(4):
            p=p*l[i-k][j+k]
        if p>max:
            max=p
        p=1


print(max)
