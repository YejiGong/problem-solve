import sys
n=int(sys.stdin.readline())
num_lists=set(sys.stdin.readline().split())
m=int(sys.stdin.readline())
num_case=sys.stdin.readline().split()

for i in num_case:
    if i in num_lists:
        print("1")
    else:
        print("0")
