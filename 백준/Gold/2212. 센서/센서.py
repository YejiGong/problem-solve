N = int(input())
K = int(input())
arr = list(map(int,input().split()))
arr.sort()
loc = []
for i in range(N-1):
    loc += [arr[i+1] - arr[i]]
loc.sort()
print(sum(loc[:N-K]))