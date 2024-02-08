K=input()
nums = [ord(i)-97 for i in K]
idx = 1
result = 1
while idx<len(nums):
    if nums[idx]<=nums[idx-1]:
        result+=1
    idx+=1
print(result)