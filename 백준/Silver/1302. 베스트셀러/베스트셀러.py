from collections import Counter
N= int(input())
title = [input() for _ in range(N)]
title = Counter(title)
maxVal = max(title.values())
res = sorted(title.items(), key=lambda x:(-x[1], x[0]))
print(res[0][0])
