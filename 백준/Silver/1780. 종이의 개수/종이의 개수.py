import sys
input = sys.stdin.readline
n = int(input())
papers=[]
for _ in range(n):
    tmp = list(map(int,input().split()))
    papers.append(tmp)

answer=[0,0,0]

def dfs(x,y,n):
    global answer
    visited = papers[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if papers[i][j] != visited:
                for k in range(3):
                    for l in range(3):
                        dfs(x+(k*n//3), y+l*n//3,n//3)
                return

    if visited == -1:
        answer[0] += 1
    elif visited == 0:
        answer[1] += 1
    else:
        answer[2] += 1

dfs(0,0,n)
for i in answer:
    print(i)


