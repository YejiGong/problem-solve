from collections import deque
import sys

input=sys.stdin.readline
nums = int(input())

for i in range(nums):
    lang = input()
    n = int(input())
    array = deque(input().rstrip()[1:-1].split(","))
    flag = True

    revtime = 0
    if n == 0:
        array = deque()
    for j in lang:
        if j=="R":
            revtime+=1
        elif j=="D":
            if len(array)>0:
                if revtime %2 == 0:
                    array.popleft()
                else:
                    array.pop()
            else:
                print("error")
                flag = False
                break
    if(flag):
        if revtime%2 == 1:
            array.reverse()
        print("["+",".join(i for i in array)+"]")
