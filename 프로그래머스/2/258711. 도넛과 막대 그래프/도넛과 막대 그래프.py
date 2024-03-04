def solution(edges):
    answer = [0,0,0,0]
    #0=정점 번호, 1=도넛 모양 그래프 수, 2=막대 모양 그래프 수, 3=8자 모양 그래프 수
    #정점 -> in은 없고 out만 있다. 
    #[0,0]에서 0은 out되는 개수. 1은 in되는 개수.
    graph={}
    for in_, out_ in edges:
        if(in_ not in graph.keys()):
            graph[in_] = [1,0]
        else:
            graph[in_][0]+=1
        if(out_ not in graph.keys()):
            graph[out_] = [0,1]
        else:
            graph[out_][1]+=1
    
    for key, counts in graph.items():
        if counts[0]>=2 and counts[1]==0:
            answer[0] = key
        if counts[0]==0 and counts[1]>0:
            answer[2]+=1
        if counts[0]>=2 and counts[1]>=2:
            answer[3]+=1
    answer[1] = graph[answer[0]][0] - answer[2] - answer[3]
    return answer