L, P = map(int,input().split())
num = list(map(int,input().split()))
res = L*P
for i in range(5):
    print(num[i] - res, end=' ')