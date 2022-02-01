n=int(input())
k=bin(n)[2:]
l=''
for i in k:
    if i=='0':
        l+='1'
    else:
        l+='0'
l=bin(int(l,2)+1)[2:]
x='0'*(32-len(k))+k
if len(l)<len(k):
    l='0'*(len(k)-len(l))+l
y='1'*(32-len(l))+l

num=0
for i in range(32):
    if x[i]!=y[i]:
        num+=1
        
print(num)
