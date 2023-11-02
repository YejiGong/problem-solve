import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
C=int(input())
def dfs(x, position, res): #depth -> position
    global ans
    if x==11:
        return
    if position==11:
        ans = max(ans, res)
        return
    dfs(x+1, position, res) #이번 선수는 해당 포지션에 선택하지 않음
    if(tc[x][position]!=0 and visited[x]==0):
        visited[x]=1
        dfs(0, position+1, res+tc[x][position]) #이번 선수를 해당 포지션에 선택함
        visited[x]=0

for _ in range(C):
    ans = 0
    visited=[0 for _ in range(11)]
    tc = [list(map(int,input().split())) for _ in range(11)]
    dfs(0,0,0)
    print(ans)
