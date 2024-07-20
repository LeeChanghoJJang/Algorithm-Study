# 9082 지뢰찾기

def process_block(i):
    if block[i-1] and block[i] and block[i+1]:
        for j in (-1, 0, 1):
            block[i+j] -= 1
        return 1
    return 0

for _ in range(int(input())):
    N = int(input())
    block = [-1] + list(map(int, input().strip())) + [-1]
    ans = 0
    input()
    print(sum(process_block(i) for i in range(1, N+1)))