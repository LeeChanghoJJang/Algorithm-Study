# 14501 퇴사 (실버3)

# 풀이1 : 브루트-포스 (31120KB / 52ms)
def f(d, sum):
    if d == N:
        global ans; ans = max(ans, sum); return
    per = cns[d][0]; cost = cns[d][1]
    if d+per < N+1:
        f(d+per, sum+cost)
    f(d+1, sum)

N = int(input())
cns = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0; f(0, 0)
print(ans)


# 풀이2 : DP (31120KB / 44ms)
N = int(input())
DP, d = [0] * (N+6), 1

while d < N+1:
    t, p = map(int, input().split())
    # 현재에서 최선을 구한 후, 상담이 완료된 후 최선을 구함
    DP[d] = max(DP[d-1], DP[d])
    DP[d+t] = max(DP[d+t], DP[d]+p)
    d += 1

print(max(DP[:N+2]))