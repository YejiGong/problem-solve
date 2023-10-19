import sys
from itertools import combinations

def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1<<ord(char) - ord('a'))
    return bit

input = sys.stdin.readline
N, K =map(int,input().split())
words = list(input().rstrip()[4:][:-4] for _ in range(N))
bits = list(map(word2bit,words))
base_bit = word2bit('antic')

#anta, tica -> a:3, t:2, n:1, i:1, c:1
if K<5:
    print(0)
elif K==26:
    print(N)
else:
    alphabet = [1<<i for i in range(26) if not (base_bit & 1<<i)]
    ans = 0
    for combination in combinations(alphabet, K-5):
        know_bit = sum(combination) | base_bit
        cnt = 0
        for bit in bits:
            if bit & know_bit == bit:
                cnt+=1
        ans = max(ans, cnt)
    print(ans)
