
import sys
input = sys.stdin.readline

n, w = int(input()), list(map(int, input().split()))
m, b = int(input()), list(map(int, input().split()))


# 추의 최대 무게 500 추의 개수 n
dp = [['N' for _ in range((500 * j)+1)] for j in range(n+1)]
ans = []

def cal(num, weight): # 추로 판별할 수 있는 구슬의 무게를 나타내는 함수
    if num > n: # 구슬의 숫자가 주어진 구슬보다 크다면 return
        return
    if dp[num][weight] == 'Y': # 이미 같은 추의 무게와 개수로 방문했다면 return
        return
    dp[num][weight] = 'Y'

    cal(num+1, weight + w[num-1])# 추 넣기
    cal(num+1, weight)# 안넣고 그대로 진행
    cal(num+1, abs(weight - w[num-1]))# 추 다른쪽에 넣기 (무게빼기)

cal(0, 0)

for bead in b:
    if bead > 500 * n:
        print('N',end=' ')
    else:
        print(dp[n][bead],end = ' ')
