n = int(input())

nums = list(map(int,input().split()))
reverse_nums=nums[::-1]

inc = [1 for _ in range(n)]
dec = [ 1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[i]>nums[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if reverse_nums[i]>reverse_nums[j]:
            dec[i] = max(dec[i], dec[j]+1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = inc[i]+dec[n-i-1]-1

print(max(result))
        
