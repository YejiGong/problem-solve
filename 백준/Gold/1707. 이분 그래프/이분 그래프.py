import sys
from collections import deque
input=sys.stdin.readline
K= int(input())
def bfs(start):
    visited[start] = 1
    queue=deque([start])
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i]==0:
                visited[i] = -1*visited[x]
                queue.append(i)
            else:
                if visited[i] == visited[x]:
                    return False
    return True

for _ in range(K):
    V, E = map(int,input().split())
    flag=True
    graph = [[] for _ in range(V+1)]
    visited=[0 for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,V+1):
        if visited[i]==0:
            if not bfs(i):
                flag=False
                break
    print("YES" if flag else "NO")
