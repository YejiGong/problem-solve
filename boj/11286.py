import sys
import heapq
N=int(sys.stdin.readline())
heap = []
for i in range(N):
    m = int(sys.stdin.readline())
    if m == 0 :
        if len(heap)!=0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(m),m))
