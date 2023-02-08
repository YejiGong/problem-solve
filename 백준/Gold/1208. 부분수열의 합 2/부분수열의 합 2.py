from itertools import combinations
from bisect import bisect_left, bisect_right

N, S = map(int,input().split())
nums = list(map(int,input().split()))

def getNum(arr, find):
    return bisect_right(arr, find) - bisect_left(arr, find)

def getSum(arr, sumArr):
    for i in range(1,len(arr)+1):
        for a in combinations(arr,i):
            sumArr.append(sum(a))
    sumArr.sort()

left, right = nums[:N//2], nums[N//2:]
leftSum, rightSum = [], []

getSum(left, leftSum)
getSum(right, rightSum)
ans = 0
for i in leftSum:
    find = S - i
    ans += getNum(rightSum, find)

ans += getNum(leftSum, S)
ans += getNum(rightSum, S)
print(ans)