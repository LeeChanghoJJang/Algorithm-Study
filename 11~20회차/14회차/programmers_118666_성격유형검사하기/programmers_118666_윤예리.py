from collections import defaultdict


def solution(survey, choices):
    personality = {
        'A': 0, 'N': 0,
        'C': 0, 'F': 0,
        'M': 0, 'J': 0,
        'R': 0, 'T': 0
    }

    for i in range(len(survey)):
        if choices[i] > 4:
            personality[survey[i][1]] += (choices[i] - 4)
        elif choices[i] < 4:
            personality[survey[i][0]] += (4 - choices[i])

    result = ''
    if personality['R'] >= personality['T']:
        result += 'R'
    else:
        result += 'T'

    if personality['C'] >= personality['F']:
        result += 'C'
    else:
        result += 'F'
    if personality['J'] >= personality['M']:
        result += 'J'
    else:
        result += 'M'
    if personality['A'] >= personality['N']:
        result += 'A'
    else:
        result += 'N'

    return result