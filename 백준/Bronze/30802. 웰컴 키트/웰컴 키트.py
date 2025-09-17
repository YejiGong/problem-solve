N = int(input())
nums = list(map(int,input().split()))
T, P = map(int,input().split())

t_res = 0
for i in nums:
    if(i%T == 0):
        t_res += i//T
    else:
        t_res += (i//T) + 1

p_res = N//P
p_res_p = N%P

print(t_res)
print(p_res, p_res_p)