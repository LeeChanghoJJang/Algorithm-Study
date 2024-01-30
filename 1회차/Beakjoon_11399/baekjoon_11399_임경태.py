# 11399 ATM
# N명의 사람 / i번 사람이 돈을 인출하는데 걸리는 시간 P_i분
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 구하기
# 최대수부터 거꾸로 적립되어 합산하는 매커니즘
# 예시) 최소시간 = 4*1 + 3*2 + 3*3 + 2*4 + 1*5

N = int(input())
P = sorted(list(map(int, input().split())), reverse=True)
min_sum = 0

# 사람 수 만큼 순회
for i in range(len(P)):
    min_sum += P[i] * (i+1)

print(min_sum)