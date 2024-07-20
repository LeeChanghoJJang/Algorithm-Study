# 9082 지뢰찾기

def process_block(block, j, N):
    # 첫 번째 블록인 경우, 현재 블록과 다음 블록이 0이 아니면 감소시킴
    if j == 0 and block[j] and block[j+1]:
        block[j] -= 1
        block[j+1] -= 1
        return 1
    # 마지막 블록인 경우, 현재 블록과 이전 블록이 0이 아니면 감소시킴
    elif j == N-1 and block[j] and block[j-1]:
        block[j] -= 1
        block[j-1] -= 1
        return 1
    # 중간 블록인 경우, 이전, 현재, 다음 블록이 0이 아니면 감소시킴
    elif 1 <= j <= N-2 and block[j-1] and block[j] and block[j+1]:
        block[j] -= 1
        block[j-1] -= 1
        block[j+1] -= 1
        return 1
    return 0

for _ in range(int(input())):
    N = int(input())
    block = list(map(int, input()))
    _ = input()
    ans = 0

    for j in range(N):
        ans += process_block(block, j, N)

    print(ans)