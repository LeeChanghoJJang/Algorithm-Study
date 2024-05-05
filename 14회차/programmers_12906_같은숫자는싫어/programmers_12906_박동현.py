# 같은 숫자는 싫어

def solution(arr):
    answer = []
    for i in arr :
        if answer and answer[-1] == i :
            continue
        else :
            answer.append(i)
    return answer