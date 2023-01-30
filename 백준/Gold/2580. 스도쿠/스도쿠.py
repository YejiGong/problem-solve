sdoku = []
blank = []


def checkRow(x, a):
    for p in range(9):
        if a == sdoku[x][p]:
            return False
    return True


def checkCol(y, a):
    for p in range(9):
        if a == sdoku[p][y]:
            return False
    return True


def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for p in range(3):
        for q in range(3):
            if a == sdoku[nx + p][ny + q]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for p in range(9):
            print(*sdoku[p])
        exit(0)

    for p in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, p) and checkCol(y, p) and checkRect(x, y, p):
            sdoku[x][y] = p
            dfs(idx + 1)
            sdoku[x][y]=0

sdoku=[list(map(int,input().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            blank.append((i, j))

dfs(0)
