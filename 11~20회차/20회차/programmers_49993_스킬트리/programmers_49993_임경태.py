# 49993 스킬트리
def check(skill, user_skill):
    for s in user_skill:
        # 현재 스킬이 skill에 없으면 다음 스킬로 넘어감
        if s not in skill: continue
        
        # 현재 스킬이 skill의 첫 번째 스킬과 같으면 선행 스킬 충족
        if s == skill[0]:
            skill = skill.replace(s, '')
        # 올바른 순서가 아니면 0 반환
        else:
            return 0

    # 모든 스킬이 올바른 순서면 1 반환
    return 1

def solution(skill, skill_trees):
    ans = 0
    for user_skill in skill_trees:
        ans += check(skill, user_skill)
    return ans

'''
    핵심 : 주어진 스킬 순서를 기준으로 각 스킬 트리가 그 순서를 지키는지 확인
'''