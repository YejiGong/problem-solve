T = int(input())
for _ in range(T):
    N = int(input())
    vic_a = 0
    vic_b = 0
    for i in range(N):
        a, b = map(str, input().split())
        if a == b:
            continue
        elif a == 'R' and b == 'S':
            vic_a += 1
        elif a == 'R' and b == 'P':
            vic_b += 1
        elif a == 'S' and b == 'R':
            vic_b += 1
        elif a == 'S' and b == 'P':
            vic_a += 1
        elif a == 'P' and b == 'S':
            vic_b += 1
        elif a == 'P' and b == 'R':
            vic_a += 1
    if vic_b == vic_a:
        print("TIE")
    elif vic_b > vic_a:
        print("Player 2")
    elif vic_b < vic_a:
        print("Player 1")