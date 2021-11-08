def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
def digit_sum(n):
    sum=0
    for i in str(n):
        print(i)
        sum=sum+int(i)
    return sum

print(digit_sum(fac(100)))
