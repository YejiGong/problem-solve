for _ in range(int(input())):
    n,m = map(int,input().split())
    gameScore = [[0,0] for _ in range(n)]
    W = []
    for _ in range(m):
        a,b,p,q = map(int,input().split())
        gameScore[a-1][0]+=p
        gameScore[a-1][1]+=q
        gameScore[b-1][0]+=q
        gameScore[b-1][1]+=p
    for i in range(n):
        if gameScore[i][0]==0 and gameScore[i][1]==0:
            W.append(0)
        else:
            W.append(1000*gameScore[i][0]**2/(gameScore[i][0]**2+gameScore[i][1]**2))
    print(int(max(W)))
    print(int(min(W)))