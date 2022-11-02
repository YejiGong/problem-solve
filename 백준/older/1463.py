import sys
n=int(sys.stdin.readline())
case=0
lists=[float("inf") for i in range(n+1)]
lists[1]=0
for i in range(1,n):
    if i+1<=n and lists[i]+1<lists[i+1]:
        lists[i+1]=lists[i]+1
    if 3*i<=n and lists[i]+1<lists[3*i]:
        lists[3*i]=lists[i]+1
    if 2*i<=n and lists[i]+1<lists[2*i]:
        lists[2*i]=lists[i]+1
print(lists[n])
