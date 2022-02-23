from collections import Counter

n=int(input())
n_card=list(map(int,input().split()))
m=int(input())
m_card=list(map(int,input().split()))

c=Counter(n_card)
for i in range(m):
    if m_card[i] in c:
        print(c[m_card[i]], end=' ')
    else:
        print('0', end=' ')
