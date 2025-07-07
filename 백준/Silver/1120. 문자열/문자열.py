def check_diff(tmp, basic):
    diff = 0
    for i in range(len(tmp)):
        if tmp[i] != basic[i]:
            diff += 1
    return diff;

A,B = map(str,input().split())
res = len(B)
len_diff = len(B) - len(A)+1
for i in range(len_diff):
    res = min(res, check_diff(A, B[i:i+len(A)]))
print(res)

