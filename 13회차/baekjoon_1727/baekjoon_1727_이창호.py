import sys

# 입력 파일을 열어서 stdin으로 설정합니다.
sys.stdin = open('input.txt')

# 남자와 여자의 인원 수를 입력 받습니다.
n, m = map(int, input().split())

# 남자와 여자의 점수를 입력 받습니다.
# 0번 인덱스는 사용하지 않으므로, 각 리스트의 맨 앞에 0을 추가합니다.
mans = [0] + list(map(int, input().split()))
womans = [0] + list(map(int, input().split()))

# 남자와 여자의 점수를 오름차순으로 정렬합니다.
mans.sort()
womans.sort()

# DP 테이블을 초기화합니다. (n+1) x (m+1) 크기의 2차원 배열로 생성합니다.
# dp[i][j]는 남자 i명과 여자 j명 사이의 최소 매칭 점수를 의미합니다.
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 남자 i명과 여자 1명 사이의 최소 매칭 점수를 계산합니다.
# 이는 남자 i명과 첫 번째 여자 사이의 거리의 합과 같습니다.
for x in range(1, n + 1):
    dp[x][1] = dp[x - 1][1] + abs(mans[x] - womans[1])

# DP를 이용하여 최소 매칭 점수를 계산합니다.
for x in range(1, n + 1):
    for y in range(2, m + 1):
        if x == y:
            # 남자와 여자의 수가 같을 때, 이전 상태의 점수에 현재 매칭의 거리를 더합니다.
            dp[x][y] = dp[x - 1][y - 1] + abs(mans[x] - womans[y])
        elif x > y:
            # 남자가 더 많을 때, 이전 상태의 점수에 현재 매칭의 거리를 더하거나,
            # 남자를 하나 제외한 경우의 점수 중 더 작은 값을 선택합니다.
            dp[x][y] = min(dp[x - 1][y - 1] + abs(mans[x] - womans[y]), dp[x - 1][y])
        else:
            # 여자가 더 많을 때, 이전 상태의 점수에 현재 매칭의 거리를 더하거나,
            # 여자를 하나 제외한 경우의 점수 중 더 작은 값을 선택합니다.
            dp[x][y] = min(dp[x - 1][y - 1] + abs(mans[x] - womans[y]), dp[x][y - 1])

# 결과 출력
# dp 테이블의 가장 오른쪽 아래 값이 남자와 여자 사이의 최소 매칭 점수입니다.
print(dp[-1][-1])
