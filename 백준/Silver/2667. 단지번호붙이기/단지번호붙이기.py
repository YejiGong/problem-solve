N = int(input())
maps=[list(map(int,input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']
count = 0

def dfs(x, y):
    global N, count
    if x<0 or x>=N or y<0 or y>=N:
        return False

    if maps[x][y] ==1 and visited[x][y] ==0:
        count +=1
        visited[x][y]=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx, ny)
        return True
    return False

results = []

for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            results.append(count)
            count = 0
results.sort()
print(len(results))
for i in results:
    print(i)