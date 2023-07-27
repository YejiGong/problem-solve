N=int(input())
nums=list(map(int,input().split()))
result = [-1 for _ in range(N)]
queue = [[0,nums[0]]]
for i in range(1,N):
    while queue:
        if queue[-1][1] < nums[i]:
            result[queue[-1][0]]=nums[i]
            queue.pop()
        else:
            break
    queue.append([i,nums[i]])

print(*result)