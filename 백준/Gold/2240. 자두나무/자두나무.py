T,W = map(int,input().split())
tree_one = [0]+[0 for _ in range(T)]
tree_two = [0]+[0 for _ in range(T)]
for t in range(T):
    tree = int(input())
    if tree==1:
        tree_one[t+1]=1
    else:
        tree_two[t+1]=1

dp=[[0 for _ in range(T+1)] for _ in range(W+1)]
W1=[0 for _ in range(T+1)]
W2=[0 for _ in range(T+1)]
for i in range(T+1):
    if(i==0):
        W1[i] = sum(tree_one)
        W2[i] = sum(tree_two)
    else:
        W1[i] = sum(tree_one[:i])+sum(tree_two[i:])
        W2[i] = sum(tree_two[:i])+sum(tree_one[i:])
        dp[1][i] = max(W1[i], dp[1][i-1])
dp[1][0]=W1[0]
for i in range(2,W+1):
    for j in range(1,T+1):
        if(i%2==0):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]+W2[j]-W2[0])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]+W1[j]-W1[0])
maxVal = dp[1][0]
for i in range(1,W+1):
    maxVal = max(maxVal, dp[i][-1])
print(maxVal)