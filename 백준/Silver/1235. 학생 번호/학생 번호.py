n=int(input())
nums = list(input() for _ in range(n))

for i in range(1, len(nums[0])+1):
    results=[]
    for j in range(n):
        if nums[j][-i:] in results:
            break
        else:
            results.append(nums[j][-i:])
    if len(results)==n:
        print(i)
        break