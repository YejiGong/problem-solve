import sys
input=sys.stdin.readline
N=int(input())
nums=[list(map(int,input().split())) for _ in range(N)]
same_class=[0 for _ in range(N)]
visited=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        for k in range(5):
            if nums[i][k] == nums[j][k] and visited[i][j]==0:
                same_class[i]+=1
                same_class[j]+=1
                visited[i][j] = 1
                visited[j][i] = 1
print(same_class.index(max(same_class))+1)