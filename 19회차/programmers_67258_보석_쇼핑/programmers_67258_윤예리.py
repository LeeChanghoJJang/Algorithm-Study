def solution(gems):
    start = 0
    end = 0

    gem_set = list(set(gems))
    n = len(gem_set)

    gem_dict = {gems[0]: 1}
    answer = [1, len(gems)]
    while start <= end and end < len(gems):
        if len(gem_dict) == n:
            if answer[1] - answer[0] > end - start:
                answer = [start+1, end+1]

            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1

        elif len(gem_dict) < n:
            end += 1
            if end >= len(gems):
                break
            if gems[end] not in gem_dict:
                gem_dict[gems[end]] = 1
            else:
                gem_dict[gems[end]] += 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))