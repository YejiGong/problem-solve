N=int(input())
M=int(input())
S=input()
result = []
for i in range(1,M-1):
    if S[i]=='O' and S[i-1]=='I' and S[i+1]=='I':
        result.append(i)
if(N==1):
    print(len(result))
else:
    if(len(result)>0):
        idx = result[0]
        cnt = 1
        res = 0
        for i in range(1,len(result)):
            if result[i]-idx == 2:
                idx = result[i]
                cnt+=1
            else:
                #4일때 N=2면 3개,4일때 N=3이면 2개, 4일때 N=4면 1개.
                if(cnt>=N):
                    res += cnt-N+1
                idx = result[i]
                cnt = 1
        if(cnt>=N):
            res += cnt-N+1
        print(res)
    else:
        print(0)
