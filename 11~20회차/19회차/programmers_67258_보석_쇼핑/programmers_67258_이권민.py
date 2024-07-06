import math

min_result = list()
min_range = math.inf


def solution(gems):
    gems_kind = set(gems)

    if len(gems_kind) == 1:
        return [1, 1]

    visited = [False] * len(gems)
    combination(visited, 0, 0, len(gems_kind), gems)

    answer = list()
    while min_result:
        x, y = min_result.pop()
        if y - x == min_range:
            answer.append([x + 1, y + 1])
    answer.sort()

    return answer[0]


def combination(visited: list, s, depth, gems_kind, gems):
    global min_range
    if depth == 2:
        s_e = list()
        for i in range(len(visited)):
            if visited[i]:
                s_e.append(i)
        if len(set(gems[s_e[0]: s_e[1] + 1])) == gems_kind:
            if min_range >= s_e[1] - s_e[0]:
                min_range = s_e[1] - s_e[0]
                min_result.append([s_e[0], s_e[1]])
        return

    for i in range(s, len(visited)):
        if visited[i]:
            continue

        visited[i] = True
        combination(visited, i, depth + 1, gems_kind, gems)
        visited[i] = False