n,m,r = map(int,input().split())
item = [0]+list(map(int,input().split()))
INF = 1e9
loc = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,input().split())
    loc[a][b] = l
    loc[b][a] = l
for i in range(1,n+1):
    loc[i][i] = 0
#최소거리 구하기
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            loc[i][j]=min(loc[i][j], loc[i][k]+loc[k][j])

result=[0]+[0 for i in range(n)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if loc[i][j]<=m:
            result[i]+=item[j]
print(max(result))