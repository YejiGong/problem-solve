N=int(input())
lengths=list(map(int,input().split()))
prices = list(map(int,input().split()))
select =[0 for _ in range(N-1)]
select[0] = prices[0]
cnt = select[0]*lengths[0]
for i in range (1,N-1):
    select[i] = min(select[i-1], prices[i])
    cnt += select[i]*lengths[i]
print(cnt)
