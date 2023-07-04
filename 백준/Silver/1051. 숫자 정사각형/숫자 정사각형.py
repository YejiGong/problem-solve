
N,M = map(int,input().split())
square = [[int(i) for i in input()] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
result = 1
for x in range(N):
    for y in range(M):
        for i in range(y+1,M):
            if square[x][y] == square[x][i]:
                lenth = i-y
                if x+lenth<N and square[x][y] == square[x+lenth][y] and square[x][y] == square[x+lenth][i]:
                    result = max(result,(lenth+1)**2)
print(result)