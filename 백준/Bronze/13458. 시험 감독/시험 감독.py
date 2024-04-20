import math
N=int(input())
A=list(map(int,input().split()))
B,C = map(int,input().split())
num = N
for i in range(N):
    if(A[i]>B):
        num += math.ceil((A[i]-B)/C)
print(num)
