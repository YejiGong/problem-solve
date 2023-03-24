import sys
sys.setrecursionlimit(10**6)

def div(s,idx):
    ls=len(s)
    if ls == 3 and idx != 1:
        return '- -'
    elif ls>=3 and idx == 1:
        return s.replace('-', ' ')
    
    arr = []

    for i in range(0, ls, ls//3) :
        arr.append(strs[i:i+ls//3])
    k = div(arr[0], 0) + div(arr[1], 1) + div(arr[2], 2)
    return k

while True:
    input = sys.stdin.readline
    k = '-'
    n = input().rstrip()
    if n == '':
        break
    num = (3**int(n))
    if num == 1:
        print('-')
        continue
    strs = k*num
    arr = div(strs, 0)
    print(arr)