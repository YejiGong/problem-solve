import sys
input = sys.stdin.readline
from collections import deque
N,M = map(int,input().split())
indegree=[1]*(N+1)
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    indegree[b]+=1
    graph[a].append(b)

dp=[1 for _ in range(N+1)]
queue=deque()
for i in range(1,N+1):
    if indegree[i] == 1:
        queue.append(i)
while queue:
    cnt = queue.popleft()
    for i in graph[cnt]:
        indegree[i]-=1
        if indegree[i]==1:
            dp[i] = dp[cnt]+1
            queue.append(i)

print(*dp[1:])