d1 = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety', 1000:'onethousand'}
#approach
#first make something which works till 99

def lc99(n):
        if n in d1:
            return d1[n]
        return d1[10*(n//10)] + d1[n%10]

def lc999(n):
    if n in d1:
        return d1[n]
    elif n<100:
        return lc99(n)
    elif n%100!=0:
        return d1[n//100]+ "hundredand"+ lc99(n%100)
    else:
        return d1[n//100] + "hundred"




sum=0
for i in range(1,1000):
    print(lc999(i))
    sum=sum+len(lc999(i))

sum=sum+11
print(sum)
