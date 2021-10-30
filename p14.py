
n=13
cd={}
def cn(n):
    i=1
    while n!= 1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        i=i+1
    return i

max=0
mn=0
#improvement - store already calculated values in dictionary
for i in range(1,1000000):
    c=cn(i)
    if c>max:
        max=c
        mn=i
print(mn)
