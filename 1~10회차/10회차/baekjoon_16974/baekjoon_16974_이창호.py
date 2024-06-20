import sys
sys.stdin = open('input.txt')  # input.txt 파일을 표준 입력으로 사용

N, X = map(int, input().split())  # 햄버거의 층 수 N과 원하는 햄버거의 번호 X를 입력받습니다.

def hamburger(N, X):
    result = 0  # 결과값을 저장할 변수를 초기화합니다.
    while N >= 0:  # 층 수가 0 이상인 동안 반복합니다.
        if X == DP[N][0]:  # X가 현재 층의 패티 위치와 동일한 경우
            result += DP[N][1]  # 현재 층의 패티 개수를 결과값에 더합니다.
            return result  # 결과값을 반환합니다.
        elif X == DP[N][0] // 2 + 1:  # X가 현재 층의 패티 중간 위치와 동일한 경우
            result += DP[N][1] // 2 + 1  # 현재 층의 패티 개수의 절반에 1을 더하여 결과값에 더합니다.
            return result  # 결과값을 반환합니다.
        elif X > DP[N][0] // 2 + 1:  # X가 현재 층의 패티 중간 위치보다 큰 경우
            X -= DP[N - 1][0] + 2  # X를 조정합니다.
            result += DP[N][1] // 2 + 1  # 현재 층의 패티 개수의 절반에 1을 더하여 결과값에 더합니다.
        else:  # X가 현재 층의 패티 위치보다 작은 경우
            X -= 1  # X를 조정합니다.
        N -= 1  # 현재 층을 처리했으므로 층 수를 1 감소시킵니다.

    return result  # 최종 결과값을 반환합니다.

# DP 배열 초기화
DP = [[1, 1] for _ in range(N + 1)]  # DP 배열을 초기화합니다.
for i in range(1, N + 1):
    DP[i][0] = 2 * DP[i - 1][0] + 3  # 층마다의 패티 위치를 계산합니다.
    DP[i][1] = 2 * DP[i - 1][1] + 1  # 층마다의 패티 개수를 계산합니다.

print(hamburger(N, X))  # 결과를 출력합니다.
