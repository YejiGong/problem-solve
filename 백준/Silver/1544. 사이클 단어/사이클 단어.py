import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
word = []
for i in range(n):
    word.append(input().rstrip())

for i in range(n):
    dq = deque(word[i])
    while True:
        dq.append(dq.popleft())
        save = "".join(dq)
        if save == word[i]:
            break
        if save in word:
            idx = word.index(save)
            word.pop(idx)
            word.insert(idx, word[i])
word = set(word)
print(len(word))