L = int(input())
N = int(input())
arr = [0 for _ in range(L + 1)]
mx = 0
mx_i = 0
for n in range(N):
    P, K = map(int, input().split())
    if K - P > mx:
        mx_i = n + 1
        mx = K - P
    for i in range(P, K + 1):
        if arr[i] == 0:
            arr[i] = n + 1
print(mx_i)
real = 0
real_i = 0
for i in range(1, N + 1):
    x = arr.count(i)
    if x > real:
        real = x
        real_i = i
print(real_i)