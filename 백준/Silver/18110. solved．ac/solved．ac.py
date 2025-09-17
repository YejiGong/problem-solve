import math
import sys
input = sys.stdin.readline
n = int(input())
comments = list(int(input()) for _ in range(n))
comments.sort()
num = math.floor((n * 0.15)+0.5)
new_comments = comments[num:len(comments)-num]
if(len(new_comments) == 0):
    print(0)
else:
    print(math.floor((sum(new_comments)/len(new_comments)) + 0.5))