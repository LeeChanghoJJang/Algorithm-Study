T = int(input())

for tc in range(T):
    N, M, K, A, B = map(int, input().split())

    reception_list = list(map(int, input().split()))
    repair_list = list(map(int, input().split()))
    time_list = sorted(map(int, input().split()))

    memo_list = [[-1, -1] for _ in range(K)]
    table_reception = [0] * N
    table_repair = [0] * M
    wait_list = []
    result = 0

    A -= 1
    B -= 1

    for i, t in enumerate(time_list):
        min_i, min_ = -1, float('inf')

        for j, v in enumerate(table_reception):
            if min_ > v:
                min_i = j
                min_ = v

            if v <= t:
                min_i = j
                min_ = v
                break

        table_reception[min_i] = max(table_reception[min_i], t) + reception_list[min_i]
        wait_list.append((table_reception[min_i], min_i, i))
        memo_list[i][0] = min_i

    wait_list.sort()
    for t, _, i in wait_list:
        min_i, min_ = -1, float('inf')

        for j, v in enumerate(table_repair):
            if min_ > v:
                min_i = j
                min_ = v

            if v <= t:
                min_i = j
                min_ = v
                break

        table_repair[min_i] = max(table_repair[min_i], t) + repair_list[min_i]
        memo_list[i][1] = min_i

    for i, (f, s) in enumerate(memo_list, start = 1):
        if f == A and s == B:
            result += i

    print(f'#{tc + 1} {result if result else -1}')