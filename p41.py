"""

"""

#find all primes till 
#if you need more than that then do manual compute

from itertools import permutations
def isprime(n):
    for i in range(2,int(n/2+1)):
        if n%i == 0:
            return False
    return True
digits=['1','2','3','4','5','6','7','8','9']
l=[]
for i in range(1,9):
    a=permutations(digits[0:i+1])
    a=[list(x) for x in a]
    a=[''.join(x) for x in a]
    a=[int(x) for x in a]
    l.extend(a)
max = 0
l.sort()
for x in reversed(l):
    print(x)
    if isprime(x):
        print(x)
        break
#find all permutation 10 digits, then 9 digits, etc
#check if that is prime
