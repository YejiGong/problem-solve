n = int(input())
ans = [0 for _ in range(26)]

for i in range(n):
    cnt = [[0 for _ in range(26)] for _ in range(2)]
    a, b = input().split()
    for j in a:
        cnt[0][ord(j)-97] += 1
    for j in b:
        cnt[1][ord(j)-97] += 1
    for j in range(26):
        ans[j] += max(cnt[0][j], cnt[1][j])
for i in range(26):
    print(ans[i])

