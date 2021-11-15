def isabd(n):
    sum=0
    n=int(n)
    for i in range(2,int(n/2)+1):
        if n%i==0:
            if n/i <= i:
                break
            sum=sum+i+n/i
        
    return n < int(sum+1)

l=[]
for i in range(1, (28123//2) + 1):
    if isabd(i):
        l.append(i)
sum=0
n=len(l)
for i in range(1, 28123+1):
    k=i//2
    for x in l:
        if x > k :
            break
        if (i-x) in l:
            sum=sum+i
            break
print(sum)

