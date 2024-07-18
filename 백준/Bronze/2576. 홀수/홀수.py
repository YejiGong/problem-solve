nums=[int(input()) for _ in range(7)]
new_nums = [i for i in nums if i%2==1]
new_nums.sort()
if(len(new_nums)==0):
    print(-1)
else:
    print(sum(new_nums))
    print(new_nums[0])