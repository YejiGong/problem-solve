def solution(m, n, startX, startY, balls):
    answer=[]
    end_li = ((-startX,startY),(startX,-startY),(m*2-startX,startY),(startX,2*n-startY)) #선대칭점
    for X,Y in balls:
        distances = []
        for endX,endY in end_li: # 대칭점들을 순회
            e_b_distance = (X-endX)**2+(Y-endY)**2 # 대칭점에서 공까지 거리
            e_s_distance = (startX-endX)**2+(startY-endY)**2 # 대칭점에서 시작까지 거리

            if not (startX==X==endX or startY==Y==endY) or (e_b_distance > e_s_distance):
                distances.append(e_b_distance)
        answer.append(min(distances)) # 대칭점까지 거리중 최솟값을 정답으로
    return answer