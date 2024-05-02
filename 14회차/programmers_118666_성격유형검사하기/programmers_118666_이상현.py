dict_ = {
    1: 3, 2: 2, 3: 1, 4: 0,
    5: 1, 6: 2, 7: 3
}

score_dict = {
    'A': 0, 'N': 0, 'C': 0, 'F': 0, 'M': 0,
    'J': 0, 'R': 0, 'T': 0, 'N': 0, 'A': 0
}

pairs = ['RT', 'CF', 'JM', 'AN']


def solution(survey, choices):
    answer = ''

    len_ = len(survey)

    for i in range(len_):
        select1 = survey[i][0]
        select2 = survey[i][1]

        if choices[i] in {1, 2, 3, 4}:
            score_dict[select1] += dict_[choices[i]]
        else:
            score_dict[select2] += dict_[choices[i]]

    for pair in pairs:
        if score_dict[pair[0]] > score_dict[pair[1]]:
            answer += pair[0]
        elif score_dict[pair[0]] < score_dict[pair[1]]:
            answer += pair[1]
        else:
            answer += pair[0] if pair[0] < pair[1] else pair[1]

    return answer