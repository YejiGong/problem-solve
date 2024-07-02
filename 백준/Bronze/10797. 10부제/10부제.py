N=int(input())
nums = list(map(int,input().split()))
result=0
for i in nums:
    if i == N:
        result+=1
print(result)