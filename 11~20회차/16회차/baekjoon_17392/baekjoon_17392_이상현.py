N, M = map(int, input().split())
list_ = list(map(int, input().split()))
sum_ = sum(list_) + N
result = 0

if sum_ >= M:
    print(0)
else:
    q = (M - sum_) // (N + 1)
    r = (M - sum_) % (N + 1)

    for i in range(1, q + 1):
        result += i ** 2 * (N + 1)

    result += (q + 1) ** 2 * r

    print(result)