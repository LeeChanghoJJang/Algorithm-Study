import sys
input = sys.stdin.readline

def bin_search(start, end, target):
    if start > end:
        return start

    mid = (start + end) // 2
    temp = result[mid]

    if temp == target:
        return mid

    elif temp > target:
        return bin_search(start, mid - 1, target)

    else:
        return bin_search(mid + 1, end, target)

N = int(input())
num_list = list(map(int, input().split()))
result = [num_list[0]]

for i in range(1, N):
    if num_list[i] > result[-1]:
        result.append(num_list[i])
    else:
        result[bin_search(0, len(result) - 1, num_list[i])] = num_list[i]

print(len(result))