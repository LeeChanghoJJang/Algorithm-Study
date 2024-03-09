# 5525 IOIOI

# KMP 알고리즘 : 100점
# 문자열을 패턴과 비교하다 틀린 부분이 나오기 전, 일치하는 부분에 집중한 알고리즘
def KMP(P, text):
    # IOIOI -> [0, 0, 1, 2, 3] 배열 생성
    # lps 배열 : 접두사 == 접미사가 될 수 있는 부분 문자열 중 가장 긴 것의 길이
    # 예시) 부분 문자열이 ABAABAB 일때 앞의 AB와 뒤의 AB가 최대한으로 같으므로 2가 된다
    # 마찬가지로 IOIOI
    # i=0 -> 부분 문자열 : I   (부분문자열 2개 생성 불가) -> 0
    # i=1 -> 부분 문자열 : IO  (일치하는 접두사 접미사 없음) -> 0
    # i=2 -> 부분 문자열 : IOI  (I가 일치) -> 1
    # i=3 -> 부분 문자열 : IOIO  (IO가 일치) -> 2
    # i=4 -> 부분 문자열 : IOIOI  (IOI가 일치) -> 3

    lps = [0] * len(P)
    for i in range(1, len(P)):
        # 패턴의 현재 인덱스의 문자가 이전 인덱스 문자에 이어서 접두사와 일치하는 부분이 있으면
        if P[lps[i-1]] == P[i]:
            # 일치부분이 1개 증가하는 것
            lps[i] = lps[i-1] + 1

    # lps 배열 적용 부분 -> KMP
    # 일치했다는 사실을 어떻게 이용할 것인가?
    # 문자 : ABCDABCDABEE
    # 패턴 : ABCDABE
    # < 바로 아래단계로 이동 (lps[5] == 2 이므로) >
    # 문자 : ABCDABCDABEE
    # 패턴 :     ABCDABE
    cnt, j = 0, 0  # cnt: 일치하는 부분의 개수 / j: 패턴에서 비교하고 있는 부분
    for i in range(len(text)):  # i: 문자열에서 비교하고 있는 부분
        # 일치했던 정보와 lps배열을 이용하여 중간 단계를 뛰어넘는 부분
        # while 문을 이용하는 이유 : 주어진 정보로 최대한 중간 단계를 뛰어넘기 위해
        # 패턴의 처음부분을 조사하지 않고 있으며 텍스트와 패턴이 일치하지 않는다면
        while j > 0 and text[i] != P[j]:
            j = lps[j - 1]
        # 텍스트와 패턴이 일치하면
        if text[i] == P[j]:
            # 패턴의 인덱스가 끝까지 도달했다면
            if j == len(P) - 1:
                #  패턴 글자에 해당하는 부분이 있다는 것이므로 카운트 +1 하고 다음으로 점프하여 탐색 진행
                cnt += 1
                j = lps[j]
            # 패턴의 인덱스가 진행중이라면 문자열의 다음부분과 패턴의 다음부분을 비교하기 위해 인덱스 증가
            else:
                j += 1
    return cnt

N, M, S = int(input()), int(input()), input()
print(KMP('I'+'OI'*N, S))

# Brute-Force : 52점
'''
N, M, S = int(input()), int(input()), input()
char, cnt = 'I' + 'OI'*N, 0
for i in range(M-len(char)+1):
    if S[i:i+len(char)] == char:
        cnt += 1
print(cnt)
'''