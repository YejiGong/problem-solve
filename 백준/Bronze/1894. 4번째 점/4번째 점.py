while(True):
    try:
        tmp = list(map(float,input().split()))
        a=(tmp[0],tmp[1])
        b=(tmp[2],tmp[3])
        c=(tmp[4],tmp[5])
        d=(tmp[6],tmp[7])
        res=[0,0]
        for i in range(2):
            if(a==c):
                res[i] = d[i]+b[i]-a[i]
            if(a==d):
                res[i] = c[i]+b[i]-a[i]
            if(b==c):
                res[i] = d[i]+a[i]-b[i]
            if(b==d):
                res[i] = c[i]+a[i]-b[i]
        print("{:.3f}".format(res[0]), "{:.3f}".format(res[1]))
    except:
        break