a=1
b=1
t=0
i=2
import math
#digits = int(math.log10(n))+1
n=0
while n<3:
    i=i+1
    t=b
    b=a+b
    a=t
    n=int(math.log10(b))+1 

print(i)
