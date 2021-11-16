"""

"""

#find all primes till 
#if you need more than that then do manual compute

from itertools import permutations
n=1000000
p=n*[1]
p[0] = 0
p[1] = 0

i=2
k=2
while i <=500000:
    while i*k < n:
        p[i*k] = 0
        k=k+1
    i=i+1
    k=2
for i in range(2,1000000):
    if p[i] == 1:
        print(i)
def perm(n):
    a=list(str(n))
    a=[int(x) for x in a]
    a=list(permutations(a))
    a=[list(x) for x in a]
    a=[ int(''.join(str(x) for x in b)) for b in a]
    return a
def cirprime(n):
   l = perm(n)
   for x in l:
       if p[x] == 0:
           return False
   return True

count = 0
print(perm(232))
for i in range(2,1000000):
    if p[i] ==1:
        if cirprime(i):
            print(i)
            count=count+1
print(count)
