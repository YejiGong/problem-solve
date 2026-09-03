from collections import deque
def solution(m, n, h, w, drops):
    INF = len(drops) + 1
    coords = [[INF for _ in range(n)] for _ in range(m)]
    for i in range(len(drops)):
        x, y= drops[i]
        coords[x][y] = i+1 
    # -----------------------------------
    # 1. 가로 w칸의 최소값
    # -----------------------------------

    row_min = []

    for i in range(m):
        dq = deque()
        mins = []

        for j in range(n):
            while dq and coords[i][dq[-1]] >= coords[i][j]:
                dq.pop()

            dq.append(j)

            if dq[0] <= j - w:
                dq.popleft()

            if j >= w - 1:
                mins.append(coords[i][dq[0]])

        row_min.append(mins)

    # -----------------------------------
    # 2. 세로 h칸의 최소값
    # -----------------------------------

    best = -1
    answer = None

    for j in range(n - w + 1):
        dq = deque()

        for i in range(m):

            while dq and row_min[dq[-1]][j] >= row_min[i][j]:
                dq.pop()

            dq.append(i)

            if dq[0] <= i - h:
                dq.popleft()

            if i >= h - 1:
                start_i = i - h + 1

                min_num = row_min[dq[0]][j]

                if min_num > best:
                    best = min_num
                    answer = [start_i, j]

                elif min_num == best and [start_i, j] < answer:
                    answer = [start_i, j]
    
    return answer
