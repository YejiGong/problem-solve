from itertools import combinations
while(True):
    case = list(map(int,input().split()))
    if case[0]==0:
        break
    else:
        result = list(combinations(case[1:],6))
        for i in result:
            print(" ".join(map(str,i)))
        print("")
