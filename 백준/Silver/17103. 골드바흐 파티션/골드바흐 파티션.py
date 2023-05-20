T = int(input())
prime = []
check = [0]*1000001
check[0] = 1
check[1] = 1

for i in range(2,1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i,1000001,i):
            check[j] = 1
for i in range(T):
    count = 0
    n = int(input())
    for i in prime:
        if i>=n:
            break
        if not check[n-i] and i<=n-i:
            count +=1
    print(count)
