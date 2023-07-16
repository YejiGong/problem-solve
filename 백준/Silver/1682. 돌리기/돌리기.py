from collections import deque
import sys
input = sys.stdin.readline
tmp = list(map(str,input().split()))
square_after = tmp[0]+tmp[1]+tmp[2]+tmp[3]+tmp[7]+tmp[6]+tmp[5]+tmp[4]
square_before='12348765'

def A(lst):
    return lst[4]+lst[5]+lst[6]+lst[7]+lst[0]+lst[1]+lst[2]+lst[3]
def B(lst):
    return lst[3]+lst[0]+lst[1]+lst[2]+lst[7]+lst[4]+lst[5]+lst[6]
def C(lst):
    return lst[0]+lst[2]+lst[6]+lst[3]+lst[4]+lst[1]+lst[5]+lst[7]
def D(lst):
    return lst[7]+lst[1]+lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[0]

def bfs():
    queue = deque([])
    queue.append([square_before, 0])
    check = set()
    check.add(square_before)
    while queue:
        cur, L = queue.popleft()
        if (cur==square_after):
            break
        tmp = [A(cur), B(cur), C(cur), D(cur)]
        for i in tmp:
            if i in check:
                continue
            else:
                queue.append([i, L+1])
                check.add(i)
    return L

if __name__=='__main__':
    print(bfs())
