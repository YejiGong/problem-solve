while True:
    try:
        x = int(input()) * (10**7) #구멍의 너비
    except:
        break
    n = int(input())
    nums = [int(input()) for _ in range(n)]  # 레고 조각의 길이 -> cm로 변환해서 저장
    nums.sort()
    # l1+l1 = x여야한다. 만약 여러개라면 l2-l1의 값이 가장 큰 것으로.
    start, end = 0, n-1
    queue = []
    while (start < n and end < n and start < end):
        if nums[start] + nums[end] == x:
            queue=[(start, end)]
            break
        else:
            if nums[start] + nums[end] > x:
                end -= 1
            elif nums[start] + nums[end] < x:
                start += 1
    if len(queue)>0:
        print("yes",nums[queue[0][0]], nums[queue[0][1]])
    else:
        print("danger")
