import heapq
n=int(input())
nums = []
for _ in range(n):
    h,o = map(int,input().split())
    nums.append((min(h,o),max(h,o)))
d=int(input())
candidate_num = []
for i in range(n):
    if nums[i][1] - nums[i][0] <=d:
        candidate_num.append(nums[i])

candidate_num.sort(key=lambda x:x[1])
ans = 0
q = []

for i in candidate_num:
    if not q:
        heapq.heappush(q,i)
    else:
        while q[0][0]<i[1] - d:
            heapq.heappop(q)
            if not q:
                break
        heapq.heappush(q,i)
    ans = max(ans, len(q))
print(ans)