import math

def find(n):
    cnt = 0
    for i in range(2,int(math.sqrt(n)+1)):
        while n%i==0:
            cnt += 1
            n//=i
    if n != 1:
        cnt += 1
    return cnt

A,B = map(int,input().split())
arr = [True for i in range(B+1)]

arr[1] = False
for i in range(2,B+1):
    if not arr[i]:
        continue
    
    for j in range(i*i, B+1, i):
        arr[j] = False

cnt = 0
for i in range(A,B+1):
    if arr[find(i)] == True:
        cnt += 1

print(cnt)