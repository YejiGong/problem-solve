import itertools
N = int(input())
results=[i for i in range(21)]
results[0] = 1
cnt_num = 0
for i in range(2,21):
    results[i] = results[i-1]*results[i]
    if results[i] >= N:
        cnt_num = i
        break

if(results[i] == N):
    print('YES')
else:
    comb = []
    for i in range(1,cnt_num+1):
        tmp = list(itertools.combinations(results[:cnt_num],i))
        comb+= tmp
    comb_ = [sum(i) for i in comb]

    if N in comb_:
        print('YES')
    else:
        print('NO')
