def is_pali(n):
    return str(n) == str(n)[::-1]

ans=0
for i in range(100,1000):
    for j in range(100,1000):
        t=i*j
        if is_pali(t) and t > ans:
            ans = t

print(ans)
