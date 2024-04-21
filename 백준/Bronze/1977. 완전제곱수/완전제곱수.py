import math
M=int(input())
N=int(input())
result = 0
result_num = -1
for i in range(M,N+1):
    tmp = math.sqrt(i)
    if(tmp == int(tmp)):
        result += i
        if(result_num==-1):
            result_num = i
if result_num!=-1:
    print(result)
    print(result_num)
else:
    print(-1)