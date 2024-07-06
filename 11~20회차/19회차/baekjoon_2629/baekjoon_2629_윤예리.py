import sys
input = sys.stdin.readline

def check(num, w):
    if num > n: return
    if dp[num][w]: return

    dp[num][w] = True
    check(num+1, w+weights[num-1])          # 추끼리 더한 값은 가능
    check(num+1, abs(w-weights[num-1]))     # 왼쪽 오른쪽에 추를 두면 뺀 값만큼 체크 가능
    check(num+1, w)                         # 추 없이 체크 가능


n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))
# i 번재까지의 추로 j 무게를 만들 수 있는지
dp = [[False] * 15001 for _ in range(31)]
check(0, 0)

for marble in marbles:
    if marble > 15000:  # 인덱스 에러
        print('N', end=' ')
        continue
    if dp[n][marble]:
        print('Y', end=' ')
        continue
    print('N', end=' ')