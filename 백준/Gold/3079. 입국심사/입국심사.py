import sys
input= sys.stdin.readline
N,M = map(int,input().split())
time = list(int(input()) for _ in range(N))
start, end = min(time), max(time)*M
ans = end
while start<=end:
    total = 0
    mid = (start+end)//2
    for i in range(N):
        total += mid//time[i]
    if total>=M:
        end = mid -1
        ans = min(mid,ans)
    else:
        start = mid +1

print(ans)