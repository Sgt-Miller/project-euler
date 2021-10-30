def dig_sum(n):
    sum=0
    while(n>0):
        print(n)
        sum=sum+(n%10)
        n=int(n//10)
    return sum

print(dig_sum(2**1000))
