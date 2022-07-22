string=input()
n=len(string)
result=0
for i in range(n):
    tmp=[]
    for j in range(n-i):
        tmp.append(string[j:j+i+1])
    result+=len(set(tmp))
print(result)
