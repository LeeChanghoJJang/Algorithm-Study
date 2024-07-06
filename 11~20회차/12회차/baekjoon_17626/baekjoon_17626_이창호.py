import sys

# 표준 입력을 'input.txt'에서 읽도록 재지정
sys.stdin = open('input.txt')

# 정수를 입력으로 받음
n = int(input())

# 동적 프로그래밍을 위한 리스트 초기화
DP = [0] * (n + 1)

# n보다 작거나 같은 제곱수들의 리스트 생성
squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)][::-1]

# 2부터 n까지 반복
for i in range(2, n + 1):
    min_value = float('inf')  # 최솟값 초기화
    # 제곱수들을 순회하며 최소값 계산
    for square in squares:
        if square > i:  # 제곱수가 i보다 크면 루프 종료
            break
        min_value = min(min_value, DP[i - square])  # 현재값과 DP[i - square] 중 최솟값 선택
    DP[i] = min_value + 1  # 현재 위치에서의 최솟값 계산하여 DP에 저장

# 결과 출력
print(DP[n])
