t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    t = bin(min(a,b))[::-1].index('1')
    print(n-t)