import sys
n, m = map(int,sys.stdin.readline().split())
pock_list=[]
pock_dict={}
for i in range(n):
    tmp=sys.stdin.readline().strip()
    pock_list.append(tmp)
    pock_dict[tmp]=i
for _ in range(m):
    tmp = sys.stdin.readline().strip()
    if tmp.isalpha():
        print(pock_dict[tmp]+1)
    else:
        tmp=int(tmp)
        print(pock_list[tmp-1])
