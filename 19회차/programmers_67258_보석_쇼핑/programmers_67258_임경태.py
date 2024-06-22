# 보석 쇼핑
def solution(gems):
    gem_dict = {gems[0]: 1}
    gem_cnt = len(set(gems))
    answer = [1, len(gems)+1]
    start = end = 0

    while end < len(gems):
        if len(gem_dict) == gem_cnt:
            # 현재 구간이 이전 구간보다 짧다면 결과 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start+1, end+1]
            # 카운트 감소
            gem_dict[gems[start]] -= 1
            # 보석의 카운트가 0이 되면 딕셔너리에서 제거
            if not gem_dict[gems[start]]:
                del gem_dict[gems[start]]
            start += 1
        else:
            end += 1
            # 카운트 증가
            if end < len(gems):
                gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1

    return answer
