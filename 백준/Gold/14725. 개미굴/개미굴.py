import sys
input = sys.stdin.readline
class Trie:
    def __init__(self):
        self.root = {}

    def add(self, nodes):
        cur = self.root

        for node in nodes:
            if node not in cur:
                cur[node] = {}
            cur = cur[node]
        cur[0] = True #리프 노드

    def travel(self, level, cur):
        if 0 in cur:
            return
        cur_child = sorted(cur)

        for ch in cur_child:
            print("--"*level + ch)
            self.travel(level+1, cur[ch])

N = int(input())
trie = Trie()
for _ in range(N):
    tmp = list(map(str,input().split()))
    tmp=tmp[1:]
    trie.add(tmp)
trie.travel(0, trie.root)