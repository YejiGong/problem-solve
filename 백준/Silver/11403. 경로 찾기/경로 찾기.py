import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

def check():
    tmp = 0
    for k in range(N):
        for a in range(N):
            if graph[k][a]==1:
                for b in range(N):
                    if graph[a][b]==1 and graph[k][b]==0:
                        tmp+=1
                        graph[k][b] = 1
    return tmp

while True:
    if check()==0:
        break
for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()