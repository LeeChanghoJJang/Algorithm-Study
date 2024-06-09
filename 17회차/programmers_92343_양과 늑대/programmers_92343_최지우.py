def solution(info, edges):
    global link

    n = len(info)
    link = {i: [] for i in range(n)}
    for p, c in edges:
        link[p].append(c)

    to = link[0]
    answer = search(0, 0, 0, info, to, 0)
    return answer


def search(cur, sheep, wolf, info, to, ans):
    a = 1
    if info[cur]:
        wolf += 1
    else:
        sheep += 1

    if wolf >= sheep:
        return ans

    ans = max(sheep, ans)

    if not to:
        return ans

    for i in to:
        to_ = to[:]
        to_.remove(i)
        for j in link[i]:
            to_.append(j)
        ans = max(search(i, sheep, wolf, info, to_, ans), ans)

    return ans



info = [0, 1, 0, 1, 1, 0, 0, 0, 0]
edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [3, 6], [4, 7], [6, 8]]
print(solution(info, edges))