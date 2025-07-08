N,M = map(int,input().split())
P = [int(input()) for _ in range(M)]
P.sort(reverse=True)
res = 0
idx = 0
for i in range(M):
    if(min(N,(i+1))*P[i]>res):
        res = P[i]*min(N,(i+1))
        idx = i

print(P[idx], res)
