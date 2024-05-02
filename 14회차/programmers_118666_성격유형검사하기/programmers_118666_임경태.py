# 성격 유형 검사하기 (2022 KAKAO TECH INTERNSHIP)

def solution(survey, choices):
    charD = {'R':0, 'T':0, 'C':0, 'F':0,
             'J':0, 'M':0, 'A':0, 'N':0}
    ans = ''

    # 설문 응답을 바탕으로 점수 집계
    for i in range(len(survey)):
        score = choices[i]
        if score < 4:
            charD[survey[i][0]] += abs(4-score)
        elif score > 4:
            charD[survey[i][1]] += abs(4-score)

    charKL = list(charD.keys())
    charVL = list(charD.values())

    # 집계 점수를 바탕으로 성격 도출
    for i in range(0, 7, 2):
        if charVL[i] >= charVL[i+1]:
            ans += charKL[i]
        elif charVL[i] < charVL[i+1]:
            ans += charKL[i+1]

    return ans