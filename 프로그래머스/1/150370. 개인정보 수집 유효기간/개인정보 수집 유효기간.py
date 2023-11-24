def day_calcul(today, monthVal):
    year, month, day = map(int,today.split("."))
    nextYear, nextDay = year, day-1
    nextMonth = month+monthVal
    if nextDay==0:
        nextDay = 28
        nextMonth -=1
    if nextMonth>12:
        nextYear += nextMonth//12
        nextMonth = nextMonth%12
    if nextMonth==0:
        nextYear -=1
        nextMonth = 12
    return [nextYear,nextMonth,nextDay]
def today_before_end(today, end):
    #today가 endday보다 이전인지 확인
    return (today[0]>end[0]) or (today[0]==end[0] and today[1]>end[1]) or (today[0]==end[0] and today[1]==end[1] and today[2]>end[2])
def solution(today, terms, privacies):
    today = list(map(int,today.split(".")))
    answer = []
    dictTerm = {}
    for i in terms:
        term, days = i.split()
        dictTerm[term] = int(days)
    for idx, i in enumerate(privacies):
        day, term = i.split()
        endDay = day_calcul(day,dictTerm[term])
        if(today_before_end(today,endDay)):
            answer.append(idx+1)
    return answer