import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = set([input() for _ in range(N)])
cnt = 0
for _ in range(M):
    tmp = input()
    if tmp in s:
        cnt += 1
print(cnt)
