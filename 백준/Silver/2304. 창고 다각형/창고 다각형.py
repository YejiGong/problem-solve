N=int(input())
heights = [list(map(int, input().split())) for _ in range(N)]
heights.sort()
max_coord, max_height = max(heights, key=lambda x:x[1])

def calculation(lst):
    result = 0
    coord, height = lst[0]

    for x,y in lst[1:]:
        if x == max_coord:
            result += abs(x-coord) * height
            return result
        if y>height:
            result += abs(x-coord) * height
            coord, height = x, y
    return result

if N==1:
    print(max_height)
else:
    left = calculation(heights)
    right = calculation(list(reversed(heights)))
    print(left + right + max_height)