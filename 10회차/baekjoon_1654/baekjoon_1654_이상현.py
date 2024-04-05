K, N = map(int, input().split())
list_ = [int(input()) for _ in range(K)]
start = 1
end = max(list_)
max_ = 0

if N == 1:
    max_ = max(list_)
else:
    while start <= end:
        mid = (start + end) // 2
        cnt = sum(elem // mid for elem in list_)

        if cnt < N:
            end = mid - 1
        else:
            max_ = max(max_, mid)
            start = mid + 1

print(max_)
