# 2473 세 용액
N = int(input())
S = sorted(map(int, input().split()))

res = float('inf')
ans = [0, 0, 0]

# 첫 번째 원소
for i in range(1, N-1):
    L = i  # 두 번째 원소
    R = N - 1  # 세 번째 원소

    while L < R:
        # 현재 원소의 합
        now = S[i-1] + S[L] + S[R]

        # 답과 현재 비교
        if res > abs(now):
            res = abs(now)
            ans = [S[i-1], S[L], S[R]]
        
        # 합이 음수이면 L 포인터를 오른쪽으로 이동
        if now < 0: L += 1
        # 합이 양수이면 R 포인터를 왼쪽으로 이동
        else: R -= 1

print(*sorted(ans))

'''
    핵심 : 하나의 포인터를 고정시켜두고 다른 포인터 두개를 투 포인터로 하여 탐색
'''