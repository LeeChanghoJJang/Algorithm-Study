def solution(edges):
    answer = [0, 0, 0, 0]
    dict_ = {}
    
    for s, e in edges:
        if s in dict_:
            dict_[s][0] += 1
        else:
            dict_[s] = [1, 0]
        
        if e in dict_:
            dict_[e][1] += 1
        else:
            dict_[e] = [0, 1]
        
    for v in dict_:
        v_info = dict_[v]
        
        if v_info[0] >= 2 and v_info[1] == 0:
            answer[0] = v
        elif v_info[0] >= 2 and v_info[1] >= 2:
            answer[3] += 1
        elif v_info[0] == 0 and v_info[1] >= 1:
            answer[2] += 1
            
    answer[1] = dict_[answer[0]][0] - answer[2] - answer[3]
    
    return answer