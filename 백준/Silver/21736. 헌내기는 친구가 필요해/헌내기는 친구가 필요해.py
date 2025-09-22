from collections import deque
N, M = map(int,input().split())
campus = []
visited = [[0 for _ in range(M)] for _ in range(N)]
cx, cy = 0,0
dx= [1,0,-1,0]
dy= [0,1,0,-1]

for i in range(N):
    tmp = list(input())
    campus.append(tmp)
    if 'I' in tmp:
        cx = i
        cy = tmp.index('I')

visited[cx][cy] = 1
deque = deque([(cx,cy)])
meetNum = 0
while deque:
    x,y = deque.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and campus[nx][ny]!='X':
            deque.append((nx, ny))
            visited[nx][ny] = 1
            if campus[nx][ny] == 'P':
                meetNum += 1

if meetNum == 0:
    print('TT')
else:
    print(meetNum)
