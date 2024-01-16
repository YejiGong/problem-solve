def taxi_distance(x1: list, x2: list) -> int:
    return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
point_1 = [-1, -1]
point_2 = [-1, -1]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            if point_1[0] == -1:
                point_1[0] = i
                point_1[1] = j
            else:
                point_2[0] = i
                point_2[1] = j
print(taxi_distance(point_1, point_2))