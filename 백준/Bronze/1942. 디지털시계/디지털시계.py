for _ in range(3):
    start, end = input().split()
    h1, m1, s1 = map(int,start.split(':'))
    h2, m2, s2 = map(int,end.split(':'))
    
    ans = 0
    while True:
        if s1 == 60 : m1 += 1; s1 = 0
        if m1 == 60 : h1 += 1; m1 = 0
        if h1 == 24 : h1 = 0
        
        x = h1*10000 + m1*100 + s1
        if x % 3 == 0 : ans += 1
        
        if (h1 == h2) and (m1 == m2) and (s1 == s2): break
        s1 += 1
        
    print(ans)