import sys
input = sys.stdin.readline
N, M = map(int,input().split())
balls = [0 for _ in range(N+1)]
for _ in range(M):
    i,j,k = map(int,input().split())
    for p in range(i,j+1):
        balls[p]=k

print(*balls[1:])