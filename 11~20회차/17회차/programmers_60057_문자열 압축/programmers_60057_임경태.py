# 문자열 압축 (2020 KAKAO BLIND RECRUITMENT)

def solution(s):
    N = len(s)
    answer = 1000 if N > 1 else 1

    # 문자 압축 단위
    for i in range(1, N//2+1):
        cnt = 1
        char = ''

        # 단위별로 순회
        for j in range(0, N, i):
            if s[j:j+i] == s[j+i:j+2*i]:
                cnt += 1
            else:
                if cnt > 1:
                    char += (str(cnt) + s[j:j+i])
                    cnt = 1
                else:
                    char += s[j:j+i]

        answer = min(answer, len(char))

    return answer