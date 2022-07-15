import sys
n= int(sys.stdin.readline())
card_num = list(map(int,sys.stdin.readline().split()))
card_num.sort()
m= int(sys.stdin.readline())
candidate = list(map(int,sys.stdin.readline().split()))

for i in candidate:
    start, end = 0, len(card_num)-1
    flag=False
    while start<=end:
        mid=(start+end)//2
        if card_num[mid]==i:
            print(1, end=' ')
            flag=True
            break
        elif card_num[mid]<i:
            start=mid+1
        else:
            end=mid-1
    if(flag==False):
        print(0, end=' ')
