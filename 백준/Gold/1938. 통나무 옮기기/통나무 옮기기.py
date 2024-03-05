import sys
from collections import deque
input = sys.stdin.readline
N=int(input())
map = []
loc=[]
dest = []
for i in range(N):
    tmp = list(input())
    map.append(tmp)
    for j in range(N):
        if tmp[j]=='B':
            loc.append((i,j))
        if tmp[j] == 'E':
            dest.append((i,j))

def check_direction(loc):
    if loc[0][1] == loc[1][1]: #세로 방향
        return 1
    else: #가로 방향
        return 0

dx=[-1,1,0,0]
dy=[0,0,-1,1]
#U,D,L,R
#T -> 중간점 제외 나머지 양 두 점: x-1,y-1 / x+1+y+1
result = 0
queue = deque([(loc,check_direction(loc),0)])
visit = set((loc[1],check_direction(loc)))
def bfs():
    global result
    while queue:
        loc, dir, num = queue.popleft()
        if(loc==dest):
            result = min(result,num) if result>0 else num
            return num
        for i in range(4):
            new_loc = []
            for x,y in loc:
                nx = x+dx[i]
                ny = y+dy[i]
                if(0<=nx<N and 0<=ny<N and map[nx][ny]!='1'):
                    new_loc.append((nx, ny))
                else:
                    break
            if len(new_loc)==3 and (new_loc[1],dir) not in visit:
                visit.add((new_loc[1],dir))
                queue.append((new_loc,dir,num+1))
        new_loc = []
        new_dir = 0 if dir==1 else 1
        flag = True
        if(loc[1][1]==loc[0][1]):
            #y값이 같다 -> 세로로 늘어져있는 중
            for x,y in loc:
                if(0<=y+1<N and 0<=y-1<N and map[x][y+1]!='1' and map[x][y-1]!='1'):
                    continue
                else:
                    flag = False
                    break
            if(flag):
                new_loc = [(loc[0][0]+1,loc[0][1]-1), loc[1],(loc[2][0]-1,loc[2][1]+1)]
                if ((new_loc[1],new_dir) not in visit):
                    visit.add((new_loc[1],new_dir))
                    queue.append((new_loc,new_dir,num+1))
        else:
            #x값이 같다 -> 가로로 늘어져있는 중
            for x,y in loc:
                if(0<=x+1<N and 0<=x-1<N and map[x+1][y]!='1' and map[x-1][y]!='1'):
                    continue
                else:
                    flag = False
                    break
            if(flag):
                new_loc = [(loc[0][0]-1, loc[0][1]+1), loc[1], (loc[2][0]+1, loc[2][1]-1)]
                if ((new_loc[1], new_dir) not in visit):
                    visit.add((new_loc[1], new_dir))
                    queue.append((new_loc, new_dir, num + 1))

bfs()
print(result)