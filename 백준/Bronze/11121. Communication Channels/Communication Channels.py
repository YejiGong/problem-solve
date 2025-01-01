def sol(origin,changed):
    for i in range(len(origin)):
        if origin[i]!=changed[i]:
            return 'ERROR'
    return 'OK'
 
if __name__ == '__main__':
    t= int(input())
    for i in range(t):
        origin, changed = input().split()
        print(sol(origin,changed))