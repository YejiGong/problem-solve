import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N=int(input())
graph=[[] for _ in range(N+1)]
parent=[i for i in range(N+1)]
dp=[[0,0] for i in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [0 for _ in range(N+1)]
def dfs(x):
    visit[x] = 1
    if len(graph[x])==0:
        dp[x][1] = 1
        dp[x][0] = 0
    else:
        for i in graph[x]:
            if visit[i] == 0:
                dfs(i)
                dp[x][1] += min(dp[i][0], dp[i][1])
                dp[x][0] += dp[i][1]
        dp[x][1] += 1
dfs(1)
print(min(dp[1][0], dp[1][1]))