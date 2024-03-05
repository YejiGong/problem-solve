def convertToSecond(h,m,s):
    return 3600*h + m*60 + s

def solution(h1, m1, s1, h2, m2, s2):
    startTime, endTime = convertToSecond(h1,m1,s1), convertToSecond(h2,m2,s2)
    ring = {}

    for t in range(convertToSecond(24,0,0)):
        ring[t] = {"cur":0,"after":0}

    prevSecond, prevMinute, prevHour = 0, 0, 0

    for t in range(1,convertToSecond(24,0,0)):
        afterCount,curCount = 0,0

        curSecond, curMinute, curHour = 6*t%360, (t/10)%360, (t/120)%360

        if  prevSecond < prevMinute and curSecond > curMinute :
            afterCount += 1
        elif prevSecond < prevMinute and curSecond == 0 :
            afterCount += 1
        elif curSecond == curMinute:
            curCount += 1

        if  prevSecond < prevHour and curSecond > curHour:
            afterCount += 1
        elif prevSecond < prevHour and curSecond == 0 :
            afterCount += 1
        elif curSecond == curHour:
            curCount += 1

        if t != 3600 * 12:
            if curCount != 0:
                ring[t]["cur"] += curCount
            if afterCount != 0:
                ring[t-1]["after"] += afterCount

        prevSecond, prevMinute, prevHour = curSecond, curMinute, curHour

    ring[0] = {"cur": 1, "after": 0}
    ring[3600 * 12] = {"cur": 1, "after": 0}

    ret = 0

    for time in range(startTime,endTime):
        if time in ring:
            ret += ring[time]["after"]
            ret += ring[time]["cur"]

    ret += ring[endTime]["cur"]
    return ret