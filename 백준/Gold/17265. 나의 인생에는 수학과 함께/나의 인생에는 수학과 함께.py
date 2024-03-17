import sys
input = sys.stdin.readline
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(str,input().split())))

dx=[0,1] #오른쪽, 아래
dy=[1,0]
minVal = 1e9
maxVal = -1e9
visit =[[0 for _ in range(N)] for _ in range(N)]
def calcul(operator, x,y):
    if operator == "+":
        return x+y
    elif operator=="-":
        return x-y
    elif operator=="*":
        return x*y

def dfs(x,y,res,operator):
    if(x==N-1 and y==N-1):
        global minVal
        global maxVal
        minVal = min(minVal,res)
        maxVal = max(maxVal,res)
        return
    for i in range(2):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0:
            visit[nx][ny]=1
            if(operator!=""): #leftVal, operator가 앞서 나옴.
                dfs(nx,ny,calcul(operator,res,int(graph[nx][ny])),"")
            else: #leftVal은 생성됨, operator 차례
                dfs(nx,ny,res,graph[nx][ny])
            visit[nx][ny]=0
visit[0][0]=1
dfs(0,0,int(graph[0][0]),"")
print(maxVal, minVal)