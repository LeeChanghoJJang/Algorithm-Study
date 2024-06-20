n = int(input())
arr = sorted(list(map(int, input().split())))
left = 0
right = n-1
value = abs(arr[left]+arr[right])
result = [arr[left], arr[right]]

while left < right:
    current_value = arr[left] + arr[right]

    if abs(current_value) < value:
        value = abs(current_value)
        result = [arr[left], arr[right]]

        if current_value == 0:
            break

    if current_value < 0:
        left += 1
    else:
        right -= 1

print(*result)