import sys
input = sys.stdin.readline
N, T = map(int,input().split())
bus = []
result = 1e9
for _ in range(N):
    S,I,C = map(int,input().split())
    time = [S+(I*c) for c in range(C)]
    if time[-1]<T:
        continue
    
    start = 0
    end = C - 1
    ans = 0
    while start<=end:
        mid = (start+end)//2
        if time[mid]>=T:
            ans = mid
            end = mid -1
        else:
            start = mid + 1
    result=min(result,time[ans]-T)

if result==1e9:
    print(-1)
else:
    print(result)