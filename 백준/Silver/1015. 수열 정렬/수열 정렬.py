import sys
input = sys.stdin.readline
N=int(input())
arr = list(map(int,input().split()))
p = [-1]*N
b = sorted(arr)
dt = {}
for i in range(N):
    tmp = b.index(arr[i])
    if arr[i] in dt.keys():
        p[i] = tmp + dt[arr[i]]
        dt[arr[i]]+=1
    else:
        p[i] = b.index(arr[i])
        dt[arr[i]]=1
print(*p)
