import sys
n, c = map(int, sys.stdin.readline().split())
coord=[]
for _ in range(n):
    coord.append(int(sys.stdin.readline()))
coord = sorted(coord)
start = 1
end = coord[-1]-coord[0]
result = 0

def binary_search(arr,start,end):
    global c, n, result
    while start<=end:
        mid = (start+end)//2
        cur = arr[0]
        cnt = 1
        
        for i in range(1,n):
            if arr[i]>=cur+mid:
                cnt+=1
                cur = arr[i]
            if cnt==c:
                break
        
        if cnt==c:
            start = mid+1
            result = mid
        else:
            end = mid -1

binary_search(coord, start, end)
print(result)
        
            
