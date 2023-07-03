N, S = map(int,input().split())
nums = list(map(int,input().split()))
result = 0

def check(idx,sum):
    if sum==S:
        global result
        result+=1

    tmp = sum
    for i in range(idx+1,N):
        check(i, tmp+nums[i])

for i in range(N):
    check(i,nums[i])

print(result)