N=int(input())
M=int(input())
S=input()
lenth = 2*N+1
keyword = ''
for i in range(lenth):
    if i%2==0:
        keyword+='I'
    else:
        keyword+='O'
result = 0
for i in range(M-lenth+1):
    if S[i:i+lenth] == keyword:
        result+=1
print(result)
