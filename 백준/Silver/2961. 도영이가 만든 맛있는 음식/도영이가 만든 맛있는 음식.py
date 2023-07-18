import sys
input = sys.stdin.readline
N= int(input())
foods = [list(map(int,input().split())) for _ in range(N)]
arr = []
result = 1e9

def dfs(depth, cnt, S, B):
    global result

    if cnt != 0:
        result = min(result, abs(S-B))

    if depth == N:
        return

    dfs(depth+1, cnt+1, S*foods[depth][0],B+foods[depth][1])
    dfs(depth+1, cnt, S, B)

dfs(0,0,1,0)
print(result)