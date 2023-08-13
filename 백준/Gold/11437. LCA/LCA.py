import sys
sys.setrecursionlimit(10**6)
LOG = 21
N=int(input())
parent=[[0]*LOG for _ in range(N+1)] #부모 노드 정보
depth = [0]*(N+1) #깊이
visited = [0]*(N+1) #계산 여부
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,dep):
    visited[x] = True
    depth[x] = dep
    for y in graph[x]:
        if visited[y]:
            continue
        parent[y][0] = x
        dfs(y,dep+1)

def set_parent():
    dfs(1,0)
    for i in range(1,LOG):
        for j in range(1,N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
def lca(a,b):
    if depth[a]>depth[b]:
        a,b = b,a
    
    for i in range(LOG-1, -1, -1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]
    
    if a==b:
        return a
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b=parent[b][i]
    return parent[a][0]

set_parent()

M= int(input())
for _ in range(M):
    a,b = map(int,input().split())
    print(lca(a,b))
