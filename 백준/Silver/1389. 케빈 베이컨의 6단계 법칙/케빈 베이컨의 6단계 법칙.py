import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, graph):
    global N
    visited=[0 for _ in range(N+1)]
    visited[start]=1
    queue = deque()
    queue.append(start)
    while queue:
        tmp = queue.popleft()
        for i in graph[tmp]:
            if visited[i]==0:
                visited[i] = visited[tmp]+1
                queue.append(i)
    return sum(visited)

result = []
for i in range(1,N+1):
    result.append(bfs(i, graph))

print(result.index(min(result))+1)
