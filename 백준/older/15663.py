from itertools import permutations
n, m = map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
rep = list(set(list(permutations(nums,m))))
rep.sort()
for i in rep:
    for j in i:
        print(j, end=' ')
    print()
    
