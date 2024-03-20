N=int(input())
mindp = [0,0,0]
maxdp = [0,0,0]
dy=[-1,0,1]
for i in range(0,N,2):
    arr = [list(map(int,input().split())) for _ in range(min(N-i,2))]
    for p in range(len(arr)):
        tmpmindp = [0,0,0]
        tmpmaxdp = [0,0,0]
        for j in range(3):
            if (j == 0):
                minVal = min(mindp[:2])
                maxVal = max(maxdp[:2])
            elif (j == 1):
                minVal = min(mindp)
                maxVal = max(maxdp)
            else:
                minVal = min(mindp[1:])
                maxVal = max(maxdp[1:])
            if(i!=0 or p!=0):
                tmpmindp[j] = minVal+arr[p][j]
                tmpmaxdp[j] = maxVal+arr[p][j]
            else:
                tmpmindp[j] = arr[p][j]
                tmpmaxdp[j] = arr[p][j]
        mindp = tmpmindp
        maxdp = tmpmaxdp

print(max(maxdp), min(mindp))