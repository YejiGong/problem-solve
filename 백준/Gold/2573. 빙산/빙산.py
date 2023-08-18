import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        result = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0:
                if graph[nx][ny]==0:
                    result+=1
                else:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
        graph[x][y] = max(graph[x][y]-result, 0)
idx = 0
while(True):
    check = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j]!=0 and visited[i][j]==0:
                visited[i][j]=1
                bfs(i,j)
                check+=1
    if check==1:
        idx+=1
    elif check>=2:
        print(idx)
        break
    elif check==0:
        print(0)
        break

