def d(n):
    sum=0
    n=int(n)
    for i in range(2,int(n/2)+1):
        if n%i==0:
            if n/i <= i:
                break
            sum=sum+i+n/i
        
    return int(sum+1)

isami = []
sum=0
for i in range(2,10000):
    if i in isami:
        continue
    dn=d(i)
    if (i!= dn) and (i == d(dn)):
        isami.append(i)
        isami.append(dn)
        sum=sum+i+dn
        print(i)
        print(dn)
print(sum)
