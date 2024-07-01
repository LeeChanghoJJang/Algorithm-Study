import sys
sys.stdin = open('input.txt')

cnt, chu_weight = int(input()),list(map(int,input().split()))
marble_cnt, marble_weight = int(input()), list(map(int,input().split()))

# 추의 무게는 최대 500이므로 [[추의 개수*500]*추의 개수]로 배열을 구성한다.
dp, r = [[0 for j in range((i + 1) * 500 + 1)] for i in range(cnt + 1)], []
# 추의 무게를 더한다.
# 추의 무게를 뺀다.
# 추를 사용하지 않는다.

def cal(num, weight):
    if num > cnt:
        return

    if dp[num][weight]:
        return

    dp[num][weight] = 1

    cal(num + 1, weight)
    cal(num + 1, weight + chu_weight[num - 1])
    cal(num + 1, abs(weight - chu_weight[num - 1]))


cal(0, 0)

for i in marble_weight:
    if i > 30 * 500:
        r.append("N")
    elif dp[cnt][i] == 1:
        r.append("Y")
    else:
        r.append("N")
print(*r)