import sys
input = sys.stdin.readline
N, M = map(int,input().split())
balls=[i for i in range(N+1)]
for _ in range(M):
    i, j = map(int,input().split())
    tmp = balls[i]
    balls[i] = balls[j]
    balls[j] = tmp

print(*balls[1:])