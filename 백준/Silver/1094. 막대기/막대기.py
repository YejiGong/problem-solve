X=int(input())
rod=[64]
while sum(rod)>X:
    rod.sort()
    rod_sub = rod.copy()
    rod_sub[0] = rod_sub[0]//2
    if(sum(rod_sub)<X):
        rod_sub.append(rod_sub[0])
    rod = rod_sub

print(len(rod))