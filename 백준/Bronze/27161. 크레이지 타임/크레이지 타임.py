import sys
input = sys.stdin.readline
N = int(input())

now = 1
addTime = 1
for i in range(N):
    result = "NO"
    S,T = map(str,input().split())
    if((S=="HOURGLASS") and (now==int(T))):
        result = "NO"
    elif(S=="HOURGLASS"):
        addTime *= -1
    else:
        if(now==int(T)):
            result="YES"
    print(now, result)
    now+=addTime
    if(now==13):
        now=1
    if(now==0):
        now=12