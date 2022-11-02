n=int(input())
wine=[]
for _ in range(n):
    wine.append(int(input()))
select=[0 for _ in range(n)]
select[0]=wine[0]
if(n>1):
    select[1]=wine[0]+wine[1]
if(n>2):
    select[2]=max(select[0]+wine[2],wine[1]+wine[2],select[1])
for i in range(3,n):
    select[i]=max(select[i-2]+wine[i],select[i-3]+wine[i-1]+wine[i],select[i-1])
print(select[n-1])
    
