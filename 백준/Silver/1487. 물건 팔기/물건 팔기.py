N = int(input())
num=[list(map(int,input().split())) for i in range(N)]
num.sort(key=lambda x:x[0])
res = 0
val = 0
for i in range(N):
    tmp = num[i][0]
    tmp_val = 0
    for j in range(0,N):
        if(num[j][0]>=tmp):
            tmp_val += max(tmp-num[j][1],0)
    if(tmp_val>val):
        res = tmp
        val = tmp_val
print(res)