N,S,P = map(int,input().split())

if(N>0):
    rank = list(map(int,input().split()))
else:
    rank = []

if(N==P and min(rank)>=S):
    print(-1)
elif(N>=1 and P>=1 and max(rank)<S):
    print(1)
else:
    rank.append(S)
    rank.sort(reverse=True)
    if(len(rank)>P):
        rank = rank[:P]
    score = [1 for _ in range(len(rank))]
    res = -1
    next = 0
    for i in range(1,len(rank)):
        if rank[i]==rank[i-1]:
            score[i] = score[i-1]
            next+=1
        else:
            score[i] = score[i-1]+1+next
            next=0

        if(rank[i] == S):
            res = score[i]
            break
    if(len(rank)==1 and rank[0]==S):
        res = 1
    print(res)