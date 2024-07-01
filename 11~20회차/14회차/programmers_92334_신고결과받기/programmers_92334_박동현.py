# 신고 결과 받기

def solution(id_list, report, k):
    answer = []
    tmp = dict()
    
    reported = dict()
    
    for rp in report :
        a,b = rp.split() # a : 신고한 사람 b : 신고 당한 사람 
        tmp[a] = tmp.get(a,set()) | {b}
    temp = []
    for a in tmp.values():
        temp.extend(list(a))
    for id in id_list :
        if temp.count(id) >= k :
            reported[id] = 1
    for id in id_list :
        i = 0
        for rptd in reported.keys() :
            if rptd in tmp.get(id,[]) :
                i+=1
        answer.append(i)
        
    return answer