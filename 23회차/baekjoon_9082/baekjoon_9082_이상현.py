def process_block(i):
    if list_[i - 1] and list_[i] and list_[i + 1]:
        for j in dir:
            list_[i + j] -= 1
        return 1
    return 0

T = int(input())
dir = [-1, 0, 1]

for _ in range(T):
    N = int(input())
    list_ = [-1] + list(map(int, input())) + [-1]
    input()

    result = 0

    for i in range(1, N + 1):
        result += process_block(i)

    print(result)