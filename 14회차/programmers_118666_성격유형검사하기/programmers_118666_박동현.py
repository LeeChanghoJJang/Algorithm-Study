# 성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    ans = dict()
    
    for i in range(len(choices)):
        if choices[i] > 4:
            ans[survey[i][1]] = ans.get(survey[i][1],0) + (choices[i]-4)
        elif choices[i] < 4:
            ans[survey[i][0]] = ans.get(survey[i][0],0) + (4-choices[i])
    
    if ans.get("R",0) < ans.get("T",0):
        answer += "T"
    else : answer += "R"
    
    if ans.get("C",0) < ans.get("F",0):
        answer += "F"
    else : answer += "C"

    if ans.get("J",0) < ans.get("M",0):
        answer += "M"
    else : answer += "J"
    
    if ans.get("A",0) < ans.get("N",0):
        answer += "N"
    else : answer += "A"
    
    return answer