import math
def solution(cap, n, deliveries, pickups):  
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    ans = 0
    cntD, cntP = 0, 0
    for i in range(n):
        cntD+= deliveries[i]
        cntP+= pickups[i]
        while cntD>0 or cntP>0:
            cntD-=cap
            cntP-=cap
            ans += (n-i)*2
    return ans