N=int(input())
pattern = input().split("*")
left_length = len(pattern[0])
right_length = len(pattern[1])
for i in range(N):
    tmp = input()
    if len(tmp)>=left_length+right_length and tmp[:left_length] == pattern[0] and tmp[-right_length:] == pattern[1]:
        print('DA')
    else:
        print('NE')