from collections import deque
import sys
n = int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
node=[1]
for i in range(n-1):
    m, k = map(int, sys.stdin.readline().split())
    graph[m].append(k)
    graph[k].append(m)

queue = deque()
queue.append(1)

visited=[0 for _ in range(n+1)]

def bfs():
    while queue:
        cnt=queue.popleft()
        for i in graph[cnt]:
            if visited[i] == 0:
                visited[i] = cnt
                queue.append(i)

bfs()
tmp = visited[2:]
for i in tmp:
    print(i)
