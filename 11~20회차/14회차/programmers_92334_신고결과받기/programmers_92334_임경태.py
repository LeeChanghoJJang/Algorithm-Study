# 신고 결과 받기 (2022 KAKAO BLIND RECRUITMENT)

# 풀이 2
def solution(id_list, report, k):
    ans = [0] * len(id_list)
    men = {i: 0 for i in id_list}

    # 신고 당한 이용자 카운트
    for char in set(report):
        user = char.split()[1]
        men[user] += 1

    # 신고 수 확인 후 신고자 카운트 및 정답 배열에 반영
    for char in set(report):
        if men[char.split()[1]] >= k:
            reporter = char.split()[0]
            reporterIdx = id_list.index(reporter)
            ans[reporterIdx] += 1

    return ans


# 풀이 1
from collections import defaultdict

def solution(id_list, report, k):
    reportNum = {i: 0 for i in id_list}
    reportMan = defaultdict(set)
    ans = [0] * len(id_list)

    # 신고 당한 이용자 카운트
    for char in set(report):
        A, B = char.split()
        reportMan[B].add(A)

    # 신고 수 확인 후 신고자 카운트
    for men in reportMan.values():
        if len(men) >= k:
            for man in men:
                reportNum[man] += 1

    # 정답 배열에 반영
    for idx, id in enumerate(id_list):
        ans[idx] = reportNum[id]

    return ans