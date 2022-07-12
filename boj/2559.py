n, k = map(int, input().split())
num = list(map(int, input().split()))
cnt=[0 for _ in range(n)]
cnt[0]=num[0]
result=cnt[0]
for i in range(1,n):
    cnt[i]=cnt[i-1]+num[i]
    if i==k-1:
        result=cnt[i]
    if i>=k:
        result=max(result, cnt[i]-cnt[i-k])
print(result)
