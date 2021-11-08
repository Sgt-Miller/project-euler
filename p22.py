f=open('names.txt','r')
l=f.read().split(',')
l=[x.strip('\"') for x in l]
l.sort()

sum=0
n=1
def score(word):
    sum=0
    for i in word:
        sum=sum+ord(i)-64
    return sum
for i in l:
    sum=sum+n*score(i)
    n=n+1
print(sum)

