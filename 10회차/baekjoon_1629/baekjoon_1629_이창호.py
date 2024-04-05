import sys
sys.stdin = open('input.txt')

# 입력으로 주어진 세 개의 정수를 A, B, C에 할당합니다.
A, B, C = map(int, input().split())

# 모듈러 지수 연산을 효율적으로 수행하는 함수를 정의합니다.
def power_mod(A, B, C):
    # 결과를 저장할 변수를 1로 초기화합니다.
    result = 1
    # base에는 A를 C로 나눈 나머지를 할당합니다.
    base = A % C

    # B가 0보다 클 때까지 반복합니다.
    while B > 0:
        # B가 홀수일 때, 결과에 base를 곱하고 C로 나눈 나머지를 구하여 결과 변수에 할당합니다.
        if B % 2 == 1:
            result = (result * base) % C
        # base를 제곱하고 C로 나눈 나머지를 base 변수에 할당합니다.
        base = (base * base) % C
        # B를 절반으로 나눕니다.
        B //= 2

    # 최종적으로 결과를 반환합니다.
    return result

# 함수를 호출하고 결과를 출력합니다.
print(power_mod(A, B, C))
