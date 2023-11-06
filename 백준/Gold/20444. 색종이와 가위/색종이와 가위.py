import math
n,k = map(int,input().split())
check = n*n - 4*(k-n-1)
if check>=0:
    ans_1 = (n+check**0.5)/2
    ans_2 = (n-check**0.5)/2
    if int(check**0.5)**2==check and ans_1==int(ans_1) and ans_2==int(ans_2) and ans_1>=0 and ans_2>=0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")