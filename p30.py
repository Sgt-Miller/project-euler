"""


Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def d5sum(n):
    n=str(n)
    sum=0
    for x in n:
        sum=sum+int(x)**5
    return sum


#7*(9**5) is a six digit number
#so these numbers must be less than 7 digits
sum=0
for i in range(2, 999999):
    print(i)
    if i == d5sum(i):
        sum=sum+i
print(sum)
