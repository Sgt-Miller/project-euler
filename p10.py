"""


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


from math import sqrt
q=2  
primes=[2] 
def next_prime(n):
    n=n+1
    while not isprime(n):
        n=n+1
    primes.append(n)
    return n
def isprime(n):
    for i in primes:
        if i>sqrt(n):
            break;
        if (n%i == 0):
            return False
    return True
sum=0
while q < 2000000:
    
    sum=sum+q
    print(q)
    q=next_prime(q)

print(sum)

