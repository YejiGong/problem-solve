a, b = map(int,input().split())
result=0
while b>a:
    if str(b)[-1] == '1':
        b=b//10
    elif b%2==0:
        b=b//2
    else:
        break
    result+=1
if b==a:
    print(result+1)
else:
    print(-1)
