import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    tmp = list(map(int,input().split()))
    for i in range(1,tmp[0]):
        graph[tmp[i]].append(tmp[i+1])
        indegree[tmp[i+1]] +=1



queue = deque()
res = []
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    num = queue.popleft()
    res.append(num)
    for i in graph[num]:
        indegree[i] -=1

        if indegree[i] == 0:
            queue.append(i)

if len(res)!=N:
    print(0)
else:
    for i in res:
        print(i)