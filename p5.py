"""


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


i=2520

j=1
while j <=20:
    if not (i%j == 0):
        i=i+2520
        j=1
    else:
        j=j+1



print(i)


#make it more scalable, calculate the 2520 thing 
