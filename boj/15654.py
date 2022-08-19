from itertools import permutations
n, m = map(int,input().split())
nums=list(map(int,input().split()))
perm = list(permutations(nums,m))
perm.sort()
for i in perm:
    for j in i:
        print(j, end=' ')
    print()
    
