from itertools import combinations

n, c = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# 두 그룹으로 나눠서 계산
group1, group2 = arr[:n//2], arr[n//2:]
sum1, sum2 = [], []

cnt = 1

# 첫 번째 그룹에서 부분집합의 합을 구함
for i in range(1, len(group1)+1):
    for j in combinations(group1, i):
        total = sum(j)
        # c보다 작으면 저장
        if total <= c:
            sum1.append(total)
# 두 번째 그룹
for i in range(1, len(group2)+1):
    for j in combinations(group2, i):
        total = sum(j)
        if total <= c:
            sum2.append(total)
sum2.sort()


# 두 번째 그룹에서 이분 탐색 수행해서 가능한 부분집합의 개수 구하기
for i in sum1:
    start, end = 0, len(sum2)

    while start < end:
        mid = (start+end)//2

        if i + sum2[mid] <= c:
            start = mid + 1
        else:
            end = mid
    cnt += end

print(len(sum1)+len(sum2)+cnt)
