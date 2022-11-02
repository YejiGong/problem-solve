N = int(input())
nums=[]
dp=[0 for _ in range(N)]
for _ in range(N):
    m, k = map(int, input().split())
    nums.append((m,k, abs(m-k)))
nums.sort(key = lambda x:x[0])

nums_b = []
for i in nums:
    nums_b.append(i[1])

for i in range(N):
    for j in range(i):
        if nums_b[i]>nums_b[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i]+=1

print(N-max(dp))
