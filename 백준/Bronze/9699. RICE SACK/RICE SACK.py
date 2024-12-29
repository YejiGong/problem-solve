for i in range(1, int(input()) + 1) :
    print("Case #{:d}: {:d}".format(i, max([*map(int, input().split())])))
