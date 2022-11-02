import sys
fir=sys.stdin.readline().strip().upper()
sec=sys.stdin.readline().strip().upper()
dp=[[0]*(len(sec)+1) for i in range(len(fir)+1)]

for i in range(1,len(fir)+1):
    for j in range(1,len(sec)+1):
        #i-1번까지의 문자열에서 i번째 값을 추가함(문자열이므로 i-1)
        if fir[i-1]==sec[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])
            #ACAYKP, CAPCAK에서 만약 i=2,j=2이라하자.
            #AC, CA므로 A와 CA사이의 LCS 혹은 AC와 C사이의 LCS 중 더 큰값을 저장

print(dp[-1][-1])
