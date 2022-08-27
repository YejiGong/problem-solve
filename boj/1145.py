nums = list(map(int, input().split()))

minNum = min(nums)
cnt = 0
while True:
    cnt = 0
    for i in range(5):
        if minNum % nums[i] == 0 :
            cnt += 1
    if cnt >= 3:
        print(minNum)
        break
    minNum += 1
