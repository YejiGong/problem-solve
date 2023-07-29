import sys
from collections import deque
input = sys.stdin.readline
N,L,R = map(int,input().split())
people=[list(map(int,input().split())) for _ in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def bfs(x,y):
    global sum_tmp
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and L<=abs(people[nx][ny] - people[cx][cy])<=R:
                visited[nx][ny]=1
                boundary_tmp.append((nx,ny))
                sum_tmp+=people[nx][ny]
                queue.append((nx,ny))

result = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    boundary_tmp = []
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                boundary_tmp=[(i,j)]
                sum_tmp = people[i][j]
                bfs(i,j)
                if len(boundary_tmp)>1:
                    flag = True
                    tmp_result = sum_tmp//len(boundary_tmp)
                    for k in boundary_tmp:
                        people[k[0]][k[1]] = tmp_result
            else:
                continue
    if flag:
        result += 1
    else:
        break

print(result)






