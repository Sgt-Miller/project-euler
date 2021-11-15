"""


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""





#if a is 1, b is atleast 2 and c atleast 3
#so max value of a is 996
n=1000
n=n-4
for a in range(1,n):
    for b in range(a+1,1000-a):
        c=1000-a-b
        if (a**2+b**2==c**2) and (a+b+c==1000):
                print(a*b*c)
