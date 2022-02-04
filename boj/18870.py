import sys
n=int(input())
nums=list(map(int,sys.stdin.readline().split()))
nums_set=list(set(nums))
nums_set.sort()
dics={nums_set[i] : i for i in range(len(nums_set))}
for i in nums:
    print(dics[i], end=' ')
