n, m, l = map(int,input().split())
if (n==m==l):
    print(10000+(1000*n))
elif n==m or n==l:
    print(1000+(n*100))
elif m==l:
    print(1000+(m*100))
else:
    print(max(n,m,l)*100)
