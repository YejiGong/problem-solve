N, M = map(int,input().split())
r,c,d = map(int,input().split())
#로봇청소기 최초 좌표 (r,c) 방향 d
dy = [0,1,0,-1]
dx = [-1,0,1,0]
#북,동,남,서
graph=[list(map(int,input().split())) for _ in range(N)]
#0인 경우 청소x, 1인 경우 벽.
cx,cy = r,c #현재 위치
cnt = 0 #청소한 칸 갯수
flag = True
while flag:
    if(graph[cx][cy]==0):
        graph[cx][cy] = -1 #청소된 칸
        cnt += 1
    flag = False
    for i in range(d-1, d-5, -1):
        nx = cx + dx[i%4]
        ny = cy + dy[i%4]
        if(0<=nx<N and 0<=ny<M and graph[nx][ny]==0 and flag==False):
            flag = True
            d = i%4
            cx,cy = nx, ny
            break
    if(flag==False):
        nx = cx + dx[(d+2)%4]
        ny = cy + dy[(d+2)%4]
        if(0<=nx<N and 0<=ny<M):
            if(graph[nx][ny]==1):
                break
            else:
                cx, cy = nx, ny
                flag = True

print(cnt)

