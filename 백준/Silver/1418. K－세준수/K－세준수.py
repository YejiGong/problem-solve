N= int(input())
K= int(input())
arr = [1 for _ in range(N+1)]
for i in range(2, int(N**0.5)+1):
    if arr[i]:
        for j in range(2*i, N+1, i):
            arr[j] = 0
res_arr = [1 for _ in range(N+1)]
for i in range(2,N+1):
    if arr[i] and i>K:
        for j in range(i,N+1,i):
            res_arr[j] = 0
print(sum(res_arr) - 1)