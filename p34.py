"""


145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

"""
def fac(n):
    if n == 1 or n == 0:
        return 1
    return n* fac(n-1)

def yo(n):
    t=n
    sum=0
    while t>0:
        sum=sum+fac(t%10)
        t=t//10
    return sum == n

i=10
sum=0
while True:
    if yo(i):
        print(i)
        sum=sum+i
    i=i+1
