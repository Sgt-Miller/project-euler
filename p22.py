"""


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""
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

