l=[]
for i in range(4):
    a=input()
    a=a.split(' ')
    a=[int(x) for x in a]
    l.append(a)

print(l)

sum=0
max=0
def addc(l):
    for i in reversed(range(1,4)):
        if l[i] == l[i-1]:
            l[i] = l[i]+1
            print(l)
            return l

cur = [0,0,0,0]
while cur != [0,1,2,3]:
    for i in range(4):
        sum=sum+l[i][cur[i]]
    cur = addc(cur)
    if sum > max:
        max=sum
    sum=0

print(max)


