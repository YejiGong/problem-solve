import datetime
y,m,d = map(int,input().split())
y_d, m_d, d_d = map(int,input().split())

start = datetime.date(y,m,d)
over = datetime.date(y+1000, m,d)
end = datetime.date(y_d,m_d,d_d)

if end-start < over-start:
    print("D-{}".format((end-start).days))
else:
    print("gg")