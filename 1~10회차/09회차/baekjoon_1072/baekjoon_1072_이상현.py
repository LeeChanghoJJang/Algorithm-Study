X, Y = list(map(int, input().split()))
Z = Y * 100 // X
start = 0
end = X

if Z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2

        if (Y + mid) * 100 // (X + mid) > Z:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    print(result)