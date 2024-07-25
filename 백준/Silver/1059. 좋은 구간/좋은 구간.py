L = int(input())
nums = list(map(int,input().split()))
nums.sort()
n = int(input())
left = 0
right = 1e9
if n in nums:
    print("0")
else:
    for i in nums:
        if i<n:
            left = i
        elif i>n:
            right = i
            break
    left+=1
    right-=1
    res = 0
    print((n-left)*(right-n+1) + (right-n))