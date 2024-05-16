
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr=[]
    s_num = 0 #면접 1위의 서류 순위
    m_num = 0 #서류 1위의 면접 순위
    for _ in range(N):
        a,b = map(int,input().split())
        arr.append((a,b))
    arr.sort()
    res = 1
    s_num = arr[0][0] #최솟값
    m_num = arr[0][1] #최소값
    for i in range(1,N):
        if(m_num>arr[i][1]):
            m_num = arr[i][1]
            res +=1
    print(res)
