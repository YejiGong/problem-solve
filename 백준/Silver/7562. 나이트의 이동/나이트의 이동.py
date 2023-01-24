import sys
from collections import deque

input=sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
INF = 10e9


def answer(cx, cy, nx, ny):
    q = deque()
    q.append((cx,cy))
    s[cx][cy] = 1
    while q:
        a, b = q.popleft()
        if a==nx and b==ny:
            print(s[nx][ny] -1)
            return
        for i in range(8):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<l and 0<=y<l and s[x][y]==0:
                q.append((x,y))
                s[x][y] = s[a][b]+1


T = int(input())
for i in range(T):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    s=[[0 for _ in range(l)] for _ in range(l)]
    answer(x1, y1, x2, y2)
