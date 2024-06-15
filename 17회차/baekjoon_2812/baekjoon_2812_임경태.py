# 2812 크게 만들기

# 높은 자릿수부터 그 다음 수와 비교하여 낮으면 제거
N, K = map(int, input().split())
num = input()
S = [num[0]]

delete = 0
for i in range(1, N):

    while S and delete < K and S[-1] < num[i]:
        delete += 1
        S.pop()

    S.append(num[i])

while S and delete < K:
    delete += 1
    S.pop()

print(''.join(S))