# import sys
# sys.stdin = open('input.txt')

n = int(input())    # 첫 번째 수
result = 0
result_arr = []
for i in range(0, n+1):     # i: 두 번째 수
    arr = [n, i]
    k = 0
    while arr[k]-arr[k+1] >= 0:
        arr.append(arr[k]-arr[k+1])
        k += 1

    if len(arr)>result:
        result = len(arr)
        result_arr = arr

print(result)
print(*result_arr)