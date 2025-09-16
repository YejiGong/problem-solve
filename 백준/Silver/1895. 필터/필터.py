R,C = map(int,input().split())
pixels = [list(map(int,input().split())) for _ in range(R)]
T=int(input())
center_values =[]

for r in range(R-3+1) :
    for c in range(C-3+1) :
        median = []
        for i in range(r, r+3) :
            for j in range(c, c+3) :
                median.append(pixels[i][j])

        median.sort()
        center_values.append(median[4])
print(len([i for i in center_values if i>=T]))