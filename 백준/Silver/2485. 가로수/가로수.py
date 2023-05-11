from math import gcd
N= int(input())
dist = [int(input()) for _ in range(N)]
arr= []

for i in range(1, N):
    arr.append(dist[i]-dist[i-1])

g=arr[0]
for i in range(1,len(arr)):
    g = gcd(g,arr[i])

result = 0
for i in arr:
    result += i // g - 1
print(result)