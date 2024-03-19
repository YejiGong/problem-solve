import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
result = []
board = []

for _ in range(N):
    line = list(input())
    board.append(line)

tempBoard = copy.deepcopy(board)
for i in range(1, N):
    for j in range(1, M):
        if board[i][j] == '*':
            up = down = i
            left = right = j
            size = 0
            while True:
                up -= 1
                down += 1
                left -= 1
                right += 1
                if up >= 0 and down < N and left >= 0 and right < M and board[up][j] == '*' and board[down][j] == '*' and \
                        board[i][left] == '*' and board[i][right] == '*':
                    size += 1
                    tempBoard[up][j] = tempBoard[down][j] = tempBoard[i][left] = tempBoard[i][right] = '.'
                    result.append((i + 1, j + 1, size))
                else:
                    if size > 0:
                        tempBoard[i][j] = '.'
                    break

temp = True
for t in tempBoard:
    if '*' in t:
        temp = False
        print(-1)
        break
if temp:
    print(len(result))
    result.sort(key=lambda x: (x[0], x[1], -x[2]))
    for r in result:
        print(r[0], r[1], r[2])