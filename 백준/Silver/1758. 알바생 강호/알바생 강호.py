N = int(input())
tips = [int(input()) for _ in range(N)]
tips.sort(reverse=True)
res = 0
for i in range(N):
    res += max(tips[i] - i,0)

print(res)