N = int(input())
list_ = sorted(map(int, input().split()))
min_ = float('inf')

for i in range(N):
    rest = list_[:i] + list_[i + 1:]
    left = 0
    right = N - 2

    while left < right:
        temp = rest[left] + rest[right]

        if abs(temp + list_[i]) < min_:
            min_ = abs(temp + list_[i])
            result = [rest[left], rest[right], list_[i]]

        else:
            if temp + list_[i] < min_:
                left += 1
            else:
                right -= 1

print(*sorted(result))