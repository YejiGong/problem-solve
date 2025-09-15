M,N = map(int,input().split())
eng = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8: 'eight', 9:'nine'}
def get_eng(i):
    str_i = str(i)
    res = ''
    for i in str_i:
        res += eng[int(i)] + ' '
    return res[:-1]
nums = [(i, get_eng(i)) for i in range(M, N+1)]
nums.sort(key=lambda x:x[1])
for i in range(len(nums)):
    print(nums[i][0], end= ' ')
    if i!=0 and (i+1)%10==0:
        print()
