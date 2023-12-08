N=int(input())
output=[[] for _ in range(3)]
score = [0 for _ in range(N)]
for i in range(N):
    nums = list(map(int,input().split()))
    for j in range(3):
        output[j].append(nums[j])
for i in range(3):
    for j in range(N):
        if output[i].count(output[i][j])==1:
            score[j]+=output[i][j]

for i in score:
    print(i)