import sys
sys.setrecursionlimit(10 ** 6)
n,m,r = map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(n+1):
    graph[i].sort()

cnt = 1
def dfs(graph,r,visited):
    global cnt
    visited[r] = cnt
    for i in graph[r]:
        if not visited[i]:
            cnt+=1
            dfs(graph,i,visited)

dfs(graph,r,visited)
for i in range(1,n+1):
    print(visited[i])
