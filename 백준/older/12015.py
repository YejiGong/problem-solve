import sys
n=int(input())
nums=list(map(int,sys.stdin.readline().split()))
seq=[0]

for num in nums:
    if seq[-1]<num:
        seq.append(num)
    else:
        l, r = 0, len(seq)
        while l<r:
            mid = (l+r)//2
            if seq[mid]<num:
                l = mid+1
            else:
                r = mid
        seq[r] = num
print(len(seq)-1)
