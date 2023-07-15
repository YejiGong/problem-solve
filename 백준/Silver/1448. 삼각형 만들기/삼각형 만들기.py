import sys
input = sys.stdin.readline
N = int(input())
len = [int(input()) for _ in range(N)]
len.sort(reverse=True)
answer = -1
for i in range(N - 2):
    if len[i] < len[i + 1] + len[i + 2]:
        answer = len[i] + len[i + 1] + len[i + 2]
        break
print(answer)
