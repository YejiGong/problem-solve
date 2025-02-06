from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(x,y):
    queue = deque([(x,y)])
    res = 0
    while queue:
        x,y = queue.popleft()
        res += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1 and visited[nx][ny]==0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
    return max(1,res-1)

result = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1 or arr[i][j] == 0:
            continue
        if arr[i][j] == 1:
            result = max(result,bfs(i,j))
            cnt += 1
print(cnt)
print(result)