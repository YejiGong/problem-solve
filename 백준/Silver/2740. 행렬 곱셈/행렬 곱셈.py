import sys
input = sys.stdin.readline

a=[]
b=[]

n, m = map(int,input().split())
for _ in range(n):
    tmp=list(map(int,input().split()))
    a.append(tmp)

m, k = map(int,input().split())
for _ in range(m):
    tmp = list(map(int,input().split()))
    b.append(tmp)

c = [[0 for _ in range(k)] for _ in range(n)]

for p in range(n):
    for q in range(k):
        for r in range(m):
            c[p][q] += a[p][r]*b[r][q]

for i in range(n):
    for j in range(k):
        print(c[i][j], end=' ')
    print()