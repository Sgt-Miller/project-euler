def is_all_factors(a,list):
    prod=1
    for i in list:
        prod=prod*i
    return prod == a

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

l=[]
n=2
ques=600851475143
q=ques
while True:
    if ques%n==0 :
        l.append(n)
        ques=ques/n
        continue
    n=next_prime(n)
    if is_all_factors(q,l):
            break
print(l)
