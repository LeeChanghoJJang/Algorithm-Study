def solution(gems):
    gem_cnt = len(set(gems))
    gem_dict = {}
    start = end = 0
    answer = [0, len(gems) - 1]

    while end < len(gems):
        gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1
        end += 1

        while len(gem_dict) == gem_cnt:
            if end - start < answer[1] - answer[0] + 1:
                answer = [start, end - 1]
                
            gem_dict[gems[start]] -= 1
            
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
                
            start += 1

    return [answer[0] + 1, answer[1] + 1]