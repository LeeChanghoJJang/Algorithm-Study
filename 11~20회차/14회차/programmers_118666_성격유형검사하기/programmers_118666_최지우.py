def solution(survey, choices):
    answer = ''
    types = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]
    type_score = {tp:0 for tp in types}

    for idx, tp in enumerate(survey):
        type_score[tp] += choices[idx]-4

    if type_score['RT']-type_score['TR'] > 0:
        answer += 'T'
    else:
        answer += 'R'

    if type_score['CF']-type_score['FC'] > 0:
        answer += 'F'
    else:
        answer += 'C'

    if type_score['JM']-type_score['MJ'] > 0:
        answer += 'M'
    else:
        answer += 'J'

    if type_score['AN']-type_score['NA'] > 0:
        answer += 'N'
    else:
        answer += 'A'

    return answer


s = ["AN", "CF", "MJ", "RT", "NA"]
c = [5, 3, 2, 7, 5]

print(solution(s, c))

'''
    R / T
    C / F
    J / M
    A / N
    1 ~ 7
    R3 R2 R1 0 T1 T2 T3
    ...
'''