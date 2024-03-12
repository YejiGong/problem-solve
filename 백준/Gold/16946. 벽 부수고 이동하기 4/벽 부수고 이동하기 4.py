from collections import deque
n,m = map(int,input().split())
#1:이동 불가
dx=[1,0,-1,0]
dy=[0,1,0,-1]
graph = []
result=[[0 for _ in range(m)] for _ in range(n)]
visit =[[0 for _ in range(m)] for _ in range(n)]
zeroCnt = 0
zeros = {}
for _ in range(n):
    graph.append(list(input()))

def check(px,py,num):
    queue = deque([(px,py)])
    count = 1
    result[px][py] = num
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(0<=nx<n and 0<=ny<m and int(graph[nx][ny])==0) and visit[nx][ny]==0:
                visit[nx][ny]=1
                result[nx][ny] = num
                count += 1
                queue.append((nx,ny))
    return count

for i in range(n):
    for j in range(m):
        if int(graph[i][j])==0 and visit[i][j]==0:
            visit[i][j] = 1
            zeroCnt += 1
            zeros[zeroCnt] = check(i,j,zeroCnt)

for i in range(n):
    for j in range(m):
        if int(graph[i][j])==1:
            zerosSet = set()
            for k in range(4):
                nx,ny = i+dx[k], j+dy[k]
                if 0<=nx<n and 0<=ny<m and int(graph[nx][ny])==0 and visit[nx][ny]==1:
                    zerosSet.add(result[nx][ny])
            res = 1
            for k in zerosSet:
                res += zeros[k]
            graph[i][j] = res%10

for i in range(n):
    for j in range(m):
        print(graph[i][j], end='')
    print()
