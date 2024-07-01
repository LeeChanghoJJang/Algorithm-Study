# 42895 N으로 표현
def solution(N, number):
    # 1번 사용 가능 시
    if N == number: return 1

    DP = [set() for _ in range(8)]

    for i in range(8):
        DP[i].add(int(str(N) * (i + 1)))

    # N을 2번부터 8번까지 사용해서 만들 수 있는 숫자 계산
    for i in range(1, 8):
        for j in range(i):
            
            # DP[j]와 DP[i-j-1]의 모든 조합을 통해 숫자 생성
            for op1 in DP[j]:
                for op2 in DP[i-j-1]:
                    DP[i].add(op1 + op2)  # 덧셈
                    DP[i].add(op1 - op2)  # 뺄셈
                    DP[i].add(op1 * op2)  # 곱셈
                    if op2 != 0: DP[i].add(op1 // op2)  # 나눗셈

        # number를 만들 수 있는지 확인
        if number in DP[i]: return i + 1
    return -1

'''
    핵심 : DP를 통해 각 단계에서 가능한 모든 숫자를 효율적으로 생성하고, 최소한의 N 사용 횟수로 목표 숫자를 찾는 것
'''