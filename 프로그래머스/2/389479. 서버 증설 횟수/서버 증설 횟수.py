import collections
def solution(players, m, k):
    total_user = m
    servers = []
    answer = 0
    #기본 1개는 m명 인원 감당할 수 있도록 운영중.
    for i in range(len(players)):
        servers = [j for j in servers if j > i]
        num = players[i]
        need_server = (num//m - (len(servers))) #필요한 서버 개수에서 현재 있는 개수 제외
        if need_server > 0:
            answer += need_server
            for l in range(need_server):
                servers.append(i+k)
            total_user += (need_server*m)
    return answer