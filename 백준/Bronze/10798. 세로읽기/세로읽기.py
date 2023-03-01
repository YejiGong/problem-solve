alphas = [list(map(str,input().strip())) for _ in range(5)]
for i in range(15):
    for j in range(5):
        if len(alphas[j])>i:
            print(alphas[j][i], end='')