# 15565 귀여운 라이언

N, K = map(int, input().split())
doll = list(map(int, input().split()))

cnt = L = R = 0
ans = N + 1

# 첫 번째 인형이 라이언이면 카운트 + 1
if doll[L] == 1: cnt += 1

# 오른쪽 포인터가 끝까지 갈 때까지 반복
while R < N:
    # 조건 충족 시
    if cnt == K:
        ans = min(ans, R-L+1)  # 기록
        cnt -= (doll[L] == 1)
        L += 1
    # 조건 미충족 시
    else:
        R += 1
        cnt += (R < N and doll[R] == 1)

print(ans if ans < N+1 else -1)