import sys

input = sys.stdin.readline
N = int(input())
A = [0] + list(map(int, input().split()))

def solution(start, end):
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        visited = [False] * (N+1)
        flag = False

        stack = [1]
        visited[1] = True

        while stack:
            now = stack.pop()

            if now == N:
                flag = True
                break

            for idx in range(now+1, N+1):
                temp = (idx - now) * (1 + abs(A[now] - A[idx]))
                if temp <= mid and not visited[idx]:
                    stack.append(idx)
                    visited[idx] = True

        if flag:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

print(solution(1, (N-1) * (1 + abs(A[N] - A[1]))))