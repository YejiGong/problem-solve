import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
queue=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=0

for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            queue.append((i,j))


while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
            graph[nx][ny] = graph[x][y]+1
            queue.append((nx,ny))

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans,max(i))
print(ans-1)