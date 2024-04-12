from itertools import combinations

N, C = map(int, input().split())
list_ = list(map(int, input().split()))
result = 0

left = list_[:N // 2]
right = list_[N // 2:]

sum_left = []
for i in range(N // 2 + 1):
    temp = combinations(left, i)

    for case in temp:
        sum_ = sum(case)

        if sum_ > C:
            continue
        sum_left.append(sum_)

sum_right = []
for i in range(N - N // 2 + 1):
    temp = combinations(right, i)

    for case in temp:
        sum_ = sum(case)

        if sum_ > C:
            continue
        sum_right.append(sum_)

sum_right.sort()
len_right = len(sum_right)

for elem in sum_left:
    start, end = 0, len_right

    while start < end:
        mid = (start + end) // 2

        if elem + sum_right[mid] <= C:
            start = mid + 1
        else:
            end = mid

    result += end

print(result)