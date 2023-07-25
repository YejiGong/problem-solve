import sys
import itertools

input = sys.stdin.readline
N, M = map(int,input().split())
house_loc = []
chicken_loc = []
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j] == 1:
            house_loc.append((i,j))
        elif tmp[j] == 2:
            chicken_loc.append((i,j))

def chicken_del(chicken):
    chicken_dist = [1e9 for _ in range(len(house_loc))]
    #도시의 치킨 거리
    for i in range(len(house_loc)):
        house_x, house_y = house_loc[i][0], house_loc[i][1]
        for j in range(len(chicken)):
            chicken_x, chicken_y = chicken[j][0],chicken[j][1]
            chicken_dist[i] = min(chicken_dist[i], abs(house_x-chicken_x)+abs(house_y-chicken_y))
    return sum(chicken_dist)
comb = []
for i in range(1,M+1):
    comb.append(list(itertools.combinations(chicken_loc,i)))

result = 1e9
for i in comb:
    for j in i:
        result = min(result, chicken_del(j))

print(result)