import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
graph=[list(map(int,input().rstrip())) for _ in range(N)]
visited=[[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0]=1
queue=deque()
queue.append((0,0,0))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while queue:
    x,y,z = queue.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y][z])
        exit(0)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if graph[nx][ny] == 1 and z == 0:
            visited[nx][ny][1] = visited[x][y][0]+1
            queue.append((nx,ny,1))
        elif graph[nx][ny]==0 and visited[nx][ny][z]==0:
            visited[nx][ny][z] = visited[x][y][z]+1
            queue.append((nx,ny,z))
print(-1)