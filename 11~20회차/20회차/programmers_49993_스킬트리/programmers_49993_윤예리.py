def solution(skill, skill_trees):
    answer = 0
    parents = {}
    for i in range(len(skill)-1):
        parents[skill[i+1]] = skill[i]

    for tree in skill_trees:
        stack = []
        for st in tree:
            if st in parents:
                if parents[st] not in stack:
                    break
                    
            stack.append(st)

        if len(stack) == len(tree):
            answer += 1

    return answer