import sys
from collections import deque
input=sys.stdin.readline
N,M = map(int,input().split())
node = [[0 for _ in range(N)] for _ in range(N)]
pairs = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,r = map(int,input().split())
    pairs[a].append((b,r))
    pairs[b].append((a,r))
def bfs(a,b):
    queue=deque()
    queue.append((a,0))
    visited=[0 for _ in range(N+1)]
    visited[a] = 1
    while queue:
        v,d = queue.popleft()
        if v == b:
            return d
        for i,l in pairs[v]:
            if not visited[i]:
                visited[i] = 1
                queue.append((i,d+l))
for _ in range(M):
    a,b = map(int,input().split())
    print(bfs(a,b))
