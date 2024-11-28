import heapq

K, N = map(int, input().split())
primes = list(map(int, input().split()))

pq = []

for num in primes:
    heapq.heappush(pq, num)

for i in range(N):
    num = heapq.heappop(pq)
    for j in range(K):
        new_num = num*primes[j]
        heapq.heappush(pq, new_num)

        if num%primes[j] == 0:
            break
print(num)