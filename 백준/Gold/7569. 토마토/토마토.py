import sys
from collections import deque

input=sys.stdin.readline
M,N,H = map(int,input().split())
graph=[]
queue=deque()
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
ans=0

for i in range(H):
    tmp=[]
    for j in range(N):
        tmp.append(list(map(int,input().split())))
        for k in range(M):
            if tmp[j][k]==1:
                queue.append((i,j,k))
    graph.append(tmp)


while queue:
    x,y,z = queue.popleft()
    for i in range(6):
        nx = dx[i]+x
        ny = dy[i]+y
        nz = dz[i]+z
        if 0<=nx<H and 0<=ny<N and 0<=nz<M and graph[nx][ny][nz]==0:
            graph[nx][ny][nz] = graph[x][y][z]+1
            queue.append((nx,ny,nz))

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans,max(j))
print(ans-1)