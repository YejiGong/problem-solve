import sys
n=int(sys.stdin.readline())
def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
result=str(fact(n))
count=0
for i in range(len(result)-1,0,-1):
    if result[i]=='0':
        count+=1
    else:
        break
print(count)
