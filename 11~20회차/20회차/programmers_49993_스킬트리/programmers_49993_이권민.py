def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_lst = list(skill[::-1])
        for s in skills:
            if s in skill and s != skill_lst.pop():
                break
        else:
            answer += 1
        
        
    return answer