"""


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
def next_prime(n):
    n=n+1
    while not isprime(n):
        n=n+1
    return n
def isprime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n=10001
q=1
for i in range(n):
    q=next_prime(q)

print(q)
