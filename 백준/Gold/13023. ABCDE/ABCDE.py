from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

flag = False
visited=[0]*2001

def dfs(x, depth):
    global flag
    visited[x] = 1
    if depth==4:
        flag= True
        return
    for i in graph[x]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = 0
            
for i in range(N):
    dfs(i,0)
    visited[i] = 0
    if flag:
        break
if flag:
    print(1)
else:
    print(0)