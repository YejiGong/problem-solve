from itertools import combinations
N,M=map(int,input().split())
nums = sorted(list(map(int,input().split())))
res = list(combinations(nums,M))
for i in res:
    print(*i)
