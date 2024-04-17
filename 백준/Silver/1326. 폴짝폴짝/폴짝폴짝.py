import sys
from collections import deque

N = int(sys.stdin.readline())
bridge = list(map(int, sys.stdin.readline().split()))
start, destination = map(int, sys.stdin.readline().split())

queue = deque()
queue.append(start - 1)
check = [-1] * N
check[start - 1] = 0

break_check = False

while queue:
    now = queue.popleft()
    for n in range(N):
        if (n - now) % bridge[now] == 0 and check[n] == -1:
            queue.append(n)
            check[n] = check[now] + 1
            if n == destination - 1:
                print(check[n])
                break_check = True
                break
    if break_check:
        break

if check[destination - 1] == -1:
    print(-1)