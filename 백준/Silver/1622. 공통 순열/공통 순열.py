while True:
    try:
        a = list(i for i in input())
        b = list(i for i in input())
        a.sort()
        b.sort()
        res = ''
        if len(a)>len(b):
            for i in a:
                if i in b:
                    res += i
                    b.remove(i)
        else:
            for i in b:
                if i in a:
                    res += i
                    a.remove(i)
        print(res)
    except:
        break
