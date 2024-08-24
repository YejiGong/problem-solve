cut = int(input())
piece = 1
a = 1
for i in range(cut):
    if i%2 != 0:
        a += 1
    piece += a
print(piece)