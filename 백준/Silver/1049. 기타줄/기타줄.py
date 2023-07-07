N,M = map(int,input().split())
cnt = []
min_pac=1000
min_sin=1000
for i in range(M):
    cnt.append(list(map(int,input().split())))
    min_pac=min(min_pac,cnt[i][0])
    min_sin=min(min_sin,cnt[i][1])
ans = min(min_pac*(N//6)+min_sin*(N%6),min_sin*N)
ans = min(ans, min_pac*((N//6)+1))
print(ans)
