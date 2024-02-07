from itertools import permutations
N=int(input())
arr = [i+1 for i in range(N)]
arr = list(permutations(arr))
for i in arr:
    print(*i)