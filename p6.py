"""

The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


sum1=0
sum2=0
for i in range(101):
    sum1=sum1+i*i
    sum2=sum2+i
sum2=sum2*sum2
print(sum1)
print(sum2)
print(sum2-sum1)
