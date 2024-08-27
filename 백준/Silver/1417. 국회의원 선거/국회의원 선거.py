from queue import PriorityQueue
N= int(input())
res = 0
queue = PriorityQueue()
for i in range(N):
    tmp = int(input())
    if i==0:
        res = tmp
    else:
        queue.put(-1*tmp)
cnt = 0

while queue.qsize()>0:
    num = queue.get()
    if(abs(num) >= res):
        queue.put(-1*(abs(num)-1))
        cnt += 1
        res += 1
    else:
        break
print(cnt)