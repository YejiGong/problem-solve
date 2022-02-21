n,m=map(int,input().split())
k=int(input())
m+=k
if m+k>=60:
    n+=(m//60)
    m%=60
if n>=24:
    n-=24

print(n, m)
