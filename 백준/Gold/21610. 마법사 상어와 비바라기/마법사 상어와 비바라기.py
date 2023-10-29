import sys
from collections import deque
input = sys.stdin.readline
N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
seq=[list(map(int,input().split())) for _ in range(M)]
dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
cloud = deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])

def move(d,s):
    global cloud
    new_cloud = deque()
    while cloud:
        x,y = cloud.popleft()
        nx = (x+dx[d-1]*s)%N
        ny = (y+dy[d-1]*s)%N
        graph[nx][ny]+=1
        new_cloud.append((nx,ny))
    cloud=new_cloud

def rain():
    global cloud
    for x,y in cloud:
        for i in (1,3,5,7):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]>0:
                graph[x][y]+=1

def new_cloud():
    global cloud
    new_cloud = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j]>=2 and (i,j) not in cloud:
                graph[i][j]-=2
                new_cloud.append((i,j))
    cloud = new_cloud
for d,s in seq:
    move(d,s)
    rain()
    new_cloud()

result = 0
for i in range(N):
    for j in range(N):
        result+=graph[i][j]
print(result)
