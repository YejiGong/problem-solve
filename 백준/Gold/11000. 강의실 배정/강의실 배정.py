import heapq
import sys
input = sys.stdin.readline
N=int(input())
#1<=N<=200,000 ->O(N) 정도
dp=[0 for _ in range(N)]
num = 0
#1 3, 5 8, 3 5의 경우의 수가 주어지면??
#1 3, 2 4, 3 5, 4 6, 5 8
#0<=Si<=Ti<=10^9이기 때문에 배열 전부 만들면 메모리 초과 날 듯함..
times=[] #N개
for _ in range(N):
    S,T= map(int,input().split())
    times.append((S,T))
times.sort() #NlogN 보장
finishTimes = []
heapq.heappush(finishTimes, times[0][1])
for S,T in times[1:]:
    if(finishTimes[0]>S):
        heapq.heappush(finishTimes, T)
    else:
        heapq.heappop(finishTimes)
        heapq.heappush(finishTimes, T)
print(len(finishTimes))