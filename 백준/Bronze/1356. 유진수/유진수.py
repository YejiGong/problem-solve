N=input()
flag=False
def check(data):
    result = 1
    for i in data:
        result *= int(i)
    return result
for i in range(1,len(N)):
    if check(N[:i])==check(N[i:]):
        flag=True
        break

if(flag):
    print("YES")
else:
    print("NO")
