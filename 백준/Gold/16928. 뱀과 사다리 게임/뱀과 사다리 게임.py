import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
ladders=dict()
snakes=dict()
for _ in range(N):
    i, j = map(int,input().split())
    ladders[i] = j
for _ in range(M):
    i, j = map(int,input().split())
    snakes[i] = j
visited=[False for _ in range(101)]
board_cnt = [0 for _ in range(101)]

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        now = queue.popleft()
        for move in range(1,7):
            nx = now+move
            if 0<nx<=100 and not visited[nx]:
                if nx in ladders.keys():
                    nx = ladders[nx]
                if nx in snakes.keys():
                    nx = snakes[nx]
                if not visited[nx]:
                    queue.append(nx)
                    visited[nx] = True
                    board_cnt[nx] = board_cnt[now]+1

bfs()
print(board_cnt[100])