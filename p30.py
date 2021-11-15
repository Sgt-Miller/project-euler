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
