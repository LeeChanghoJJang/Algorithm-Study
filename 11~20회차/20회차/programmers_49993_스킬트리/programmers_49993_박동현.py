def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx = 0
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill :
                if skill[idx] != skill_tree[i]:
                    break
                else :
                    idx += 1
        else :
            answer += 1
            
    return answer