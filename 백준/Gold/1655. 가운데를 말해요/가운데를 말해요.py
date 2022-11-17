import heapq
import sys

input=sys.stdin.readline
n=int(input())
bigarr=[]
smallarr=[]

for i in range(n):
    m=int(input())
    if len(bigarr) == len(smallarr):
        heapq.heappush(bigarr, m*(-1))
    else:
        heapq.heappush(smallarr,m)

    if smallarr and bigarr[0]*(-1)>smallarr[0]:
        tmp_small = heapq.heappop(smallarr)
        tmp_big = heapq.heappop(bigarr)
        heapq.heappush(bigarr, tmp_small*(-1))
        heapq.heappush(smallarr, tmp_big*(-1))

    print(bigarr[0]*(-1))