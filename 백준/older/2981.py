from math import gcd

n=int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))
nums.sort()
nums_2=[]

for i in range(1,n):
    nums_2.append(nums[i]-nums[i-1])

gcds=nums_2[0]
for i in range(1,len(nums_2)):
    gcds = gcd(gcds,nums_2[i])

result=[]
for i in range(2,int(gcds**0.5)+1):
    if gcds%i==0:
        result.append(i)
        result.append(gcds//i)
result.append(gcds)
print(*sorted(list(set(result))))
