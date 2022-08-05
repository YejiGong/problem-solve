from collections import deque
import sys
n, m, r = map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n+1):
    graph[i].sort()

num = 1
start=deque()
def bfs(r):
    global num
    visited[r] = num;
    start.append(r)
    while(start):
        tmp = start.popleft()
        for i in graph[tmp]:
            if visited[i] == 0:
                num+=1
                visited[i] = num
                start.append(i)

bfs(r)
for i in range(1,n+1):
    print(visited[i])
