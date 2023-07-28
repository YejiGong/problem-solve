import sys
input = sys.stdin.readline
while True:
    tmp = input().rstrip()
    if tmp=="0":
        break
    else:
        if tmp == tmp[::-1]:
            print("yes")
        else:
            print("no")