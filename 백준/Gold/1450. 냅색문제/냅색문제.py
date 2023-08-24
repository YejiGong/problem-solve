
N, C = map(int,input().split())
weights = list(map(int,input().split()))
w1, w2 = weights[:N//2],weights[N//2:]
sum_1, sum_2 = [], []

def a_find(l,w):
    if l>=len(w1):
        sum_1.append(w)
        return
    a_find(l+1,w)
    a_find(l+1,w+w1[l])
def b_find(l,w):
    if l>=len(w2):
        sum_2.append(w)
        return
    b_find(l+1,w)
    b_find(l+1,w+w2[l])
def binary_search(start, end, key):
    global cnt
    while start<end:
        mid = (start+end)//2
        if sum_2[mid] <= key:
            start=mid+1
        else:
            end=mid
    return end
cnt = 0
a_find(0,0)
b_find(0,0)
sum_2.sort()
for i in sum_1:
    if C - i<0:
        continue
    cnt += (binary_search(0,len(sum_2), C-i))
print(cnt)

