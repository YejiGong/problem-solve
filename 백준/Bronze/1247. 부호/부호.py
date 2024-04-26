import sys
input = sys.stdin.readline
for i in range(3):
    N = int(input())
    result = 0
    for _ in range(N):
        result += int(input())
    if(result == 0):
        print(0)
    elif(result>0):
        print("+")
    else:
        print("-")