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
def rot(nstr):
    op=[m for m in nstr]
    nstr=[m for m in nstr] #so that it isn't same id
    for i in range(len(nstr)-1):
        op[i+1] = nstr[i]
    op[0]=nstr[len(nstr)-1]
    return ''.join(op)

def perm(n):
    l=[]
    l.append(n)
    for i in range(len(str(n))-1):
        l.append(int(rot(str(l[i]))))
    return l
def cirprime(n):
   l = perm(n)
   for x in l:
       if p[x] == 0:
           return False
   return True

count = 0
for i in range(2,1000000):
    if p[i] ==1:
        if cirprime(i):
            print(i)
            count=count+1
print(count)
