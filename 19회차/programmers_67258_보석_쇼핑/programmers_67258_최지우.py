def solution(gems):
    answer = []
    max_gem = len(set(gems))

    start = 0
    gems_dict = {}

    for idx, gem in enumerate(gems):
        gems_dict[gem] = gems_dict.setdefault(gem, 0) + 1
        end = idx + 1

        while len(gems_dict) == max_gem:
            gems_dict[gems[start]] -= 1
            if not gems_dict[gems[start]]:
                del gems_dict[gems[start]]
            start += 1
            answer.append([start, end])

    return sorted(answer, key=lambda x: (x[1]-x[0], x[0]))[0]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))