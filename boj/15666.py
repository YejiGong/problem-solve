from itertools import combinations_with_replacement
n, m = map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
rep = list(set(list(combinations_with_replacement(nums,m))))
rep.sort()
for i in rep:
    for j in i:
        print(j, end=' ')
    print()
    
