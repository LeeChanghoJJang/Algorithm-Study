import sys
sys.stdin = open('input.txt')
def custom_bisect_left(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def lis_length(sequence):
    if not sequence:
        return 0

    lis = []

    for num in sequence:
        pos = custom_bisect_left(lis, num)
        if pos < len(lis):
            lis[pos] = num
        else:
            lis.append(num)

    return len(lis)

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))
print(lis_length(A))