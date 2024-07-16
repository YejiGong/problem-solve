from collections import Counter
import math
n=int(input())
graph=[Counter(list(map(int,input().split()))) for _ in range(n)]
for i in range(n):
    if graph[i].most_common(1)[0][1] >= math.ceil(sum(graph[i].values())/2):
        print(graph[i].most_common(1)[0][0])
    else:
        print("SYJKGW")
