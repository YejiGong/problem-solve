num = 1
while True:
    n=int(input())
    if(n==0):
        break
    names = [input() for _ in range(n)]
    check = [0 for _ in range(n)]
    for _ in range(2*n-1):
        a,b = map(str, input().split())
        a = int(a)
        if(check[a-1] == 0):
            check[a-1] = 1 #뺏김
        else:
            check[a-1] = 0
    for i in range(n):
        if check[i] == 1:
            print(num, names[i])
            num+=1
