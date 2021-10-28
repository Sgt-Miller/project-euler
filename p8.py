import sys
a=sys.stdin.read()
a=list(a)
a=[int(x) for x in a if x != '\n']
g=0
ad=13
p=1
for i in range(len(a)-ad+1):
    for j in range(ad):
        p=p*a[i+j]
    if p>g:
        g=p
    p=1
print(g)
