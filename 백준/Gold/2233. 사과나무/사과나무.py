import sys

# dfs : 현재 num 노드에서 루트로 가는 dfs
def dfs(num):
    # 방문하는 조상 정점(자기 자신 포함)의 방문 횟수를 1 증가
    cnt[num] += 1
    for next in adj[num]:
        dfs(next)

# 입력부
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip()))
x, y = map(int, sys.stdin.readline().split())

# st : 스택
# convert : 현재 이진 수열의 위치가 몇번째 정점인지를 나타내는 배열
st = []
convert = [0] * (2 * n)

# num : 정점 번호
num = 0

# adj : 자식에서 부모로 향하는 단방향 인접 리스트
adj = [[] for _ in range(n)]

# cnt : 썩은 사과들이 dfs를 통해 방문하는 횟수를 저장하는 리스트
cnt = [0] * n

# height : 정점의 높이를 저장하는 배열, 작을 수록 루트에 가까움에 주의
height = [0] * n

for i in range(len(arr)):
    # 시작한다면 스택에 추가
    if arr[i] == 0:
        if st:
            # 바로 밑 노드는 부모이므로 높이 1 증가
            height[num] = height[st[-1]] + 1
        st.append(num)
        convert[i] = num
        # 정점 번호 증가
        num += 1
    # 끝난다면 밑 노드(부모 노드)와 인접 리스트로 연결
    else:
        temp = st.pop()
        convert[i] = temp
        if st:
            adj[temp].append(st[-1])

x, y = convert[x - 1], convert[y - 1]
dfs(x)
dfs(y)

# res : 모든 정점들의 방문 횟수와 깊이, 정점 번호를 저장하는 리스트
res = []
for i in range(n):
    res.append((cnt[i], height[i], i))
    
# 공통 조상 정점은 방문 횟수가 2여야 하고, 그 중에서 가장 깊이가 깊은 것이 정답이므로 정렬
res.sort(key=lambda x : (-x[0], -x[1]))

# 정답 출력
for i in range(len(arr)):
    if convert[i] == res[0][2]:
        print(i + 1, end=' ')