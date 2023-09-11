import copy
N,M= map(int,input().split())
graph=[]
cctv=[]
mode=[[],[[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[0,3]],[[0,1,2],[0,1,3],[1,2,3],[0,2,3]],[[0,1,2,3]]]
#북,동,남,서
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(N):
    data = list(map(int,input().split()))
    graph.append(data)
    for j in range(M):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j],i,j])

def fill(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx+=dx[i]
            ny+=dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny]==6:
                    break
                elif board[nx][ny]==0:
                    board[nx][ny]=7
            else:
                break

def dfs(depth,arr):
    global min_value
    
    if depth==len(cctv):
        cnt = 0
        for i in range(N):
            cnt+=arr[i].count(0)
        min_value = min(min_value,cnt)
        return
    tmp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(tmp,i,x,y)
        dfs(depth+1,tmp)
        tmp = copy.deepcopy(arr)

min_value = int(1e9)
dfs(0,graph)
print(min_value)
