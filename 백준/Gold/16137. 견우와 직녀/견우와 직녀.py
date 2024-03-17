import heapq
import sys
input = sys.stdin.readline
N,M=map(int,input().split()) #N:땅 크기, M:오작교 주기
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

#한 번 지은 오작교는 한 번만 유지할 수 있다.
#이미 오작교를 짓기로 예정한 곳, 절벽이 가로와 세로로 교차하는 곳에는 오작교를 놓을 수 없다.
#(0,0) -> (N-1,N-1)

t = 0
x,y = 0,0

#(0,0)->(N-1,N-1)에 필요한 최소 시간
#상하좌우로만 움직일 수 있으므로 대각선 횡단은 불가, 오른쪽, 아래 방향으로 움직여야 빠르게 갈 수 있을 것임. (왼쪽, 위쪽으로는 x)

def isPossibleCoord(x,y):
    row_count = 0
    col_count = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(0<=nx<N and 0<=ny<N and graph[nx][ny]==0):
            if i%2==0:
                row_count += 1
            else:
                col_count += 1
    if row_count>0 and col_count>0:
        return True
    else:
        return False
def bfs():
    queue = []
    heapq.heappush(queue, (0,0,0, False, False))
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    visit[0][0] = 0
    while queue:
        t,x,y,step,isSet = heapq.heappop(queue)
        #step = x,y가 오작교인지 확인하는 flag변수 (step==True면 이번에는 오작교 건널 수 x)
        #isSet = 새로운 오작교를 하나 만든 상태인지 확인하는 flag변수
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and (visit[nx][ny]==-1 or t+1<visit[nx][ny]):
                if graph[nx][ny]==1:
                    heapq.heappush(queue,(t+1, nx, ny, False,isSet))
                    visit[nx][ny] = t+1
                if step==True and graph[nx][ny]!=1: #0,-1,2,... 모든 오작교 후보들.
                    continue
                elif graph[nx][ny]>1: #이미 만들어진 오작교
                        nextTime = (t // graph[nx][ny] + 1) * graph[nx][ny]
                        heapq.heappush(queue,(nextTime, nx,ny, True,isSet))
                        visit[nx][ny]=nextTime
    return visit[N-1][N-1]
result = 1e9
for i in range(N):
    for j in range(N):
        if graph[i][j]==0:
            if(isPossibleCoord(i,j)==False): #가로 세로가 교차해서 오작교를 만들 수 없는 절벽은 -1으로 수정해준다.
                graph[i][j]=M
                tmp_result = bfs()
                if(tmp_result!=-1):
                    result = min(result,tmp_result)
                graph[i][j]=0

print(result)