import itertools
N,M,K = map(int,input().split())
arr = [i for i in range(N)]
NCM = len(list(itertools.combinations(arr, M)))
res = 0
for i in range(K,M+1):
    res += len(list(itertools.combinations(arr[:N-M],M-i)))*len(list(itertools.combinations(arr[:M],i)))
print(res/NCM)