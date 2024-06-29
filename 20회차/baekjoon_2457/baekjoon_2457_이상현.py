N = int(input())
list_ = sorted(list(map(int, input().split())) for _ in range(N))
day = 3, 1
i = cnt = 0

def check(flower):
    if (flower[0], flower[1]) <= day < (flower[2], flower[3]):
        return True
    return False

while i < N:
    if check(list_[i]):
        prev_end = list_[i][2], list_[i][3]

        while i < N - 1:
            if day < (list_[i + 1][0], list_[i + 1][1]):
                break
            i += 1
            prev_end = max(prev_end, (list_[i][2], list_[i][3]))

        cnt += 1
        day = prev_end

        if (11, 30) < day:
            exit(print(cnt))
    i += 1

print(0)