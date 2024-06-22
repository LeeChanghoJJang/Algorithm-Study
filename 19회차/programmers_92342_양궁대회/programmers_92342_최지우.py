def solution(n, info):
    global result

    needs = [0 for _ in range(11)]
    for idx, val in enumerate(info):
        needs[idx] = val+1

    cnt = [0 for _ in range(11)]

    shoot(0, n, info, cnt)

    if result:
        return result
    else:
        return [-1]


def shoot(idx, n, ap, ry):
    global result
    global diff

    r = ry[::]
    if idx == 11:
        if n:
            r[-1] += n
        score = get_score(ap, r)
        if score > diff:

            diff = score
            result = r
            return
        if result and score == diff:
            for i in range(10, -1, -1):
                if result[i] and result[i] >= r[i]:
                    return
                if not result[i] and r[i]:
                    break

            diff = score
            result = r

        return

    if n > ap[idx]:
        r[idx] += ap[idx] + 1
        shoot(idx+1, n-ap[idx]-1, ap, r)
    shoot(idx+1, n, ap, ry)


def get_score(ap, ry):
    score = 0
    for i in range(11):
        if ry[i] == ap[i] == 0:
            continue
        if ry[i] > ap[i]:
            score += (10-i)
        else:
            score -= (10-i)
    return score


diff = 0
result = []
n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))

'''
가장 큰 점수차로 이겨야 함 + 가장 낮은 점수를 더 많이 맞힌 경우
어피치가 높은 점수부터 오면서 0개 맞춘게 있으면, 무조건 1개 쏴야할거같다

그러고 나서 재귀 + 완탐
어피치보다 많이 쏘기 // 안쏘고 넘어가기 두개 케이스 찢어서 가면 될듯
'''
