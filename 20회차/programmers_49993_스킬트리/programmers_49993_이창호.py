def solution(skill, skill_trees):
    answer = 0
    # skill은 무조건 처음부터 나와야 한다.
    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill and s != skill_list.pop(0):
                 break
        else:
            answer+=1
    return answer