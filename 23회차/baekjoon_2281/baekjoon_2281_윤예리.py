import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

maxNum = m * m * n # 최악의 경우
dp = [maxNum] * (n+1)
dp[n] = 0

def solution(x):
    
    # 계산한 적 있으면 return
    if dp[x] < maxNum:
        return dp[x]
    
    # 남은 칸 수
    remain = m - arr[x]

    for i in range(x+1, n+1):
        if remain >= 0:

            # 얘가 마지막 이름이라면 남은 칸 수는 상관이 없으므로 0 리턴
            if i == n:
                dp[x] = 0
                break

            # 이 이름을 min(다음줄에 쓰기, 이번 줄에 쓰기)
            dp[x] = min(dp[x], remain*remain+solution(i))
            # 남은 칸 수 갱신
            remain -= arr[i] + 1

    return dp[x]

print(solution(0))
