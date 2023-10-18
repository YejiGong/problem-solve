from itertools import combinations
N=int(input())
nums=[]
if N<10:
    print(N)
else:
    for i in range(1,11):
        for comb in combinations(range(0,10),i):
            comb=list(comb)
            comb.sort(reverse=True)
            nums.append(int("".join(map(str,comb))))
    nums.sort()
    try:
        print(nums[N])
    except:
        print(-1)