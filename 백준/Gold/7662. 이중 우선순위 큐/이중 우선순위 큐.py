import heapq
import sys
input = sys.stdin.readline
T=int(input())
for _ in range(T):
    k=int(input())
    max_heap, min_heap=[], []
    visit=[False]*1000001
    for i in range(k):
        l, n = map(str,input().split())
        n=int(n)

        if l=="I":
            heapq.heappush(min_heap, (n,i))
            heapq.heappush(max_heap,(-1*n, i))
            visit[i]=True
        elif l=="D":
            if n==-1:
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif n==1:
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]]=False
                    heapq.heappop(max_heap)
    
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")