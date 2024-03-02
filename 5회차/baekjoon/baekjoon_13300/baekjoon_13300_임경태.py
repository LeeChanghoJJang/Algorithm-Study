import sys
sys.stdin = open('input.txt')

# 학생 수, 한방 배정 최대 인원 수
N, K = map(int, input().split())
cnt = [[0]*6, [0]*6]

for _ in range(N):
    S, Y = map(int, input().split()) # 성별, 학년
    cnt[S][Y-1] += 1

ans = 0
for i in cnt:
    for j in i:
        if not j % K: ans += j//K
        else: ans += j//K + 1
print(ans)