strCandidate = input()
N = len(strCandidate)

table = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    table[i][i] = 1 #자기자신이므로 i~i는 항상 팰린드롬.
    if(i<N-1 and strCandidate[i] == strCandidate[i+1]):
        table[i][i+1]=1 #i~i+1이 팰린드롬.
for i in range(N-1):
    for j in range(N-2-i):
        k = i+j+2 #i는 틈, j를 기준으로 k까지의 값의 팰린드롬을 탐색함.
        if strCandidate[j] == strCandidate[k] and table[j+1][k-1]: #j==k라면 j+1 ~ k-1까지가 팰린드롬이어야한다. 따라서 table[j+1][k-1] 확인
            table[j][k] = 1 #j~k가 팰린드롬.

dp=[0 for _ in range(N)]
dp[0] = 1
for i in range(1,N):
    min_val = dp[i-1]+1 #직전 개수에 +1을 한것 (현재 자릿수 하나를 하나의 팰린드롬으로 가정) 이 기본값 + 가장 큰 값.
    for j in range(i):
        if table[j][i]: #j~i가 팰린드롬인 경우. 즉, 0~i ~ i범위 내에서 팰린드롬인 부분 문자열이 존재할때 : 해당 부분 문자열 값에 +1해주기.
            min_val = min(min_val, dp[j-1]+1) #j-1 직전의 개수에 1을 더한 값과(~:j-1까지 분할한 것에, j+1~i로 분할), 현재 min_val 중 최솟값
    dp[i] = min_val
print(dp[-1])