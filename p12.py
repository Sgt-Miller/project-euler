def dn(n):
    d=0
    n=int(n)
    for i in range(1,int(n/2)+1):
        if n%i==0:
            if n/i <= i:
                break
            d=d+2
        
    return d

i=0
t=0
max=0
while True:
    i=i+1
    t=t+i 
    d=dn(t)
    if d>500:
        print(t)
        break


