# SWEA 12173번 금화 모으기

T = int(input())

# DP 를 이용하여 접근
for tc in range(T):
    N, M = map(int, input().split())
    # max_coin[i]는 (_ + 1) 행 i 열로 이동할 때 얻을 수 있는 최대 동전 개수를
    # 저장
    max_coin = [0] * (M + 1)

    for _ in range(N):
        # [0]을 더해주는 이유는 왼쪽에서 올 때 인덱스 에러를 방지하기 위함
        row = [0] + list(map(int, input().split()))

        # 문제의 조건에서 이동할 때는 바로 오른쪽 또는 바로 아래쪽으로만 이동할 수
        # 있다고 했으므로 각 칸에 접근하는 방법은 왼쪽에서 오거나 위쪽에서 올 수밖에
        # 없음. 
        
        # 따라서 왼쪽 칸 까지의 최댓값과 위쪽 칸 까지의 최댓값 중 더 큰 값에
        # 현재 칸의 동전 개수를 더해주면 됨
        for i in range(1, M + 1):
            max_coin[i] = max(max_coin[i - 1], max_coin[i]) + row[i]

    print(f'#{tc + 1} {max_coin[-1]}')