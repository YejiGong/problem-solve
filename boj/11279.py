import heapq
import sys
N=int(sys.stdin.readline())
heap = []
for i in range(N):
    m = int(sys.stdin.readline())
    if m == 0 :
        if len(heap)!=0:
            print(-1*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -m)
