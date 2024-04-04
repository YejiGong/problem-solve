from collections import deque
R,C = map(int,input().split())
visit=[[-1 for _ in range(C)] for _ in range(R)]
maps = []
v = [] #비버 위치
g = [] #고슴도치 위치
water=[]
stone=[]
for i in range(R):
    strs = list(input())
    maps.append(strs)
    for j in range(C):
        if strs[j]=='D':
            v = [i,j]
        elif strs[j]=='S':
            g = [i,j]
        elif strs[j]=='*':
            water.append((i,j))
            visit[i][j] = 0
        elif strs[j]=='X':
            stone.append((i,j))
#고슴도치->비버, R과 C는 <=50
dx=[1,0,-1,0]
dy=[0,1,0,-1]
waterq = deque()
waterq.append((water, 0))
while waterq:
    waters,t = waterq.popleft()
    arr=[]
    for i,j in waters:
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if 0<=nx<R and 0<=ny<C and visit[nx][ny]==-1 and maps[nx][ny]!='X' and maps[nx][ny]!='D':
                visit[nx][ny] = t+1
                arr.append((nx,ny))
    if(len(arr)>0):
        waterq.append((arr, t+1))
res = -1
queue = deque()
queue.append((g[0], g[1], 0))
while queue:
    x,y,t = queue.popleft()
    if(x==v[0] and y==v[1]):
        res= t
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<R and 0<=ny<C and (visit[nx][ny]==-1 or visit[nx][ny]>t+1) and maps[nx][ny]!='X':
            visit[nx][ny]=-2
            queue.append((nx,ny,t+1))
if(res!=-1):
    print(res)
else:
    print("KAKTUS")