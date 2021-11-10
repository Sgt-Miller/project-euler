#find all primes till 10,000,000
#if you need more than that then do manual compute
n=10000000
p=n*[1]
p[0] = 0
p[1] = 0

i=2
k=2
while i <=5000000:
    while i*k < n:
        p[i*k] = 0
        k=k+1
    i=i+1
    print(i)
    k=2
    

   
def isprime(n):
    if n < 10000000:
        return p[n]
    print("ouch")
    for i in range(2,int(n/2+1)):
        if n%i == 0:
            return False
    return True
        

def cprime(a,b):
    n=0
    while True:
        if not isprime(n**2 + a*n+b):
            return n

        n=n+1
max = 0
maxprod=0
for a in range(-999,1000):
    print(a)
    for b in range(-1000,1001):
        c = cprime(a,b)
        if c > max:
            max = c
            maxprod = a*b

print(maxprod)
