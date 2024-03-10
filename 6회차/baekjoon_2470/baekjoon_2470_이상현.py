# 백준 2470번 두 용액

N = int(input())
# 용액의 특성값을 입력받은 후 오름차순으로 정렬
temp = sorted(list(map(int, input().split())))

start = 0
end = len(temp) - 1
result = temp[start] + temp[end]

# 투 포인터 이용
while start < end:
    sum = temp[start] + temp[end]

    # 만약 기존에 저장된 값보다 현재 두 용액의 특성값의 합이
    # 0에 더 가깝다면 새로 갱신
    if abs(sum) <= abs(result):
        result = sum
        result_index = [start, end]

        if sum > 0:
            end -= 1
        if sum < 0:
            start += 1
        if sum == 0:
            break

    if abs(sum) > abs(result):
        if sum > 0:
            end -= 1
        if sum < 0:
            start += 1

print(temp[result_index[0]], temp[result_index[1]])