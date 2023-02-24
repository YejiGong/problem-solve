import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, M = map(int,input().split())
graph=[[] for i in range(N+1)]
visited=[False for i in range(N+1)]
for _ in range(M):
    u, v= map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start, dep):
    visited[start] = True
    for i in graph[start]:
        if visited[i]!=True:
            dfs(i,dep+1)

count = 0

for i in range(1,N+1):
    if not visited[i]:
        if not graph[i]: #정점에 연결된 그래프가 없을때
            count+=1
            visited[i] = True
        else:
            dfs(i,0)
            count +=1

print(count)