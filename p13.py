"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
sum=0
for i in range(100):
    a=float(input())
    sum=sum+a
print(sum)
