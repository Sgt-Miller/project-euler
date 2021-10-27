
"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

uplimit = 1000
limit = uplimit-1 # "below" 1000 

def sum_first_n(n):
    """
    Sum of first n numbers
    """
    return int(n*(n+1)/2) #int removes trailing .0 decimal


sum3 = 3 * sum_first_n( int(limit/3) ) #Sum of multiples of 3 under limit
sum5 = 5 * sum_first_n( int(limit/5) )
sum15 = 15 * sum_first_n( int(limit/15) )
ans = sum3+sum5-sum15 

print(ans)
"""
Explanation - 
The question is the same as asking for 
(sum of multiples of 5) + (sum of multiples of 3) - (sum of multiples of 15)

where all are multiples under 1000

sum of multiples of m = m*(1+2+...+n)
where n is the number of multiples of m under 1000, which is int(999/m)
Also, (1+2+..+n) = n(n+1)/2
"""

