# 개인정보 수집 유효기간 (2023 KAKAO BLIND RECRUITMENT)

def solution(today, terms, privacies):
    ans = []
    termsDict = {char[0]: int(char[2:]) * 28 for char in terms}
    nowY, nowM, nowD = map(int, today.split('.'))
    now = nowY * 28 * 12 + nowM * 28 + nowD

    for i in range(len(privacies)):
        pre, case = privacies[i].split()
        preY, preM, preD = map(int, pre.split('.'))
        pre = preY * 28 * 12 + preM * 28 + preD + termsDict[case]

        if pre <= now: ans.append(i+1)

    return ans