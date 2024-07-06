def solution(survey, choices):
    MBTI = ["TR","CF","MJ","AN"]
    tendency_dict = {i:0 for i in ["A","C","F","M","N","J","R","T"]}
    for i in range(len(survey)):
        left, right = survey[i]
        if choices[i] - 4 > 0:
            tendency_dict[right] += choices[i] - 4
        else:
            tendency_dict[left] += 4 - choices[i]
    result = ''
    for i,j in MBTI:
        if tendency_dict[i] > tendency_dict[j]:
            result += i
        elif tendency_dict[i] < tendency_dict[j]:
            result += j
        else:
            result += min(i,j)
    return result

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5,3,2,7,5]
print(solution(survey,choices))