from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
start_x, start_y = 0,0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start_x, start_y = i, j
            break
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited[start_x][start_y] = 1
queue = deque()
queue.append([start_x, start_y, 0])
res_dist = -1
flag = False
while queue and flag!=True:
    x,y,dist = queue.popleft()
    if(dist!=0 and arr[x][y] != 0):
        res_dist = dist
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx< n and 0<= ny <m and visited[nx][ny] == 0 and arr[nx][ny] != 1:
            visited[nx][ny] = 1
            if arr[nx][ny] != 0:
                res_dist = dist + 1
                flag = True
                break
            else : queue.append([nx,ny,dist+1])
        if(flag): break


if(res_dist == -1):
    print('NIE')
else:
    print('TAK')
    print(res_dist)