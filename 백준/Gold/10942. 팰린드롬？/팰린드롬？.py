import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
M = int(input())
dp=[[0 for _ in range(N)] for _ in range(N)]
for n_len in range(N):
    for start in range(N-n_len):
        end = start+n_len

        if start == end:
            dp[start][end] = 1
        elif nums[start] == nums[end]:
            if start +1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(M):
    q, a = map(int,input().split())
    print(dp[q-1][a-1])
