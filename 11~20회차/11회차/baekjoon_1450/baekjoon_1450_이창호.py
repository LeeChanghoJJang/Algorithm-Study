import sys
from itertools import combinations

input = sys.stdin.readline

# 입력 받기
n, c = map(int, input().split())  # n: 물건의 개수, c: 가방의 무게 제한
arr = list(map(int, input().split()))  # 물건의 무게 리스트

# "meet in the middle"
arr_1 = arr[:n // 2]
arr_2 = arr[n // 2:]

subsum_a = []  # 첫 번째 그룹의 부분집합 합
subsum_b = []  # 두 번째 그룹의 부분집합 합

# 첫 번째 그룹의 부분집합 합 구하기
for i in range(len(arr_1) + 1):
    comb_a = combinations(arr_1, i)  # itertools의 combinations 함수를 사용하여 부분집합 생성

    for comb in comb_a:
        subsum_a.append(sum(comb))  # 부분집합의 합을 subsum_a에 저장

# 두 번째 그룹의 부분집합 합 구하기
for i in range(len(arr_2) + 1):
    comb_b = combinations(arr_2, i)

    for comb in comb_b:
        subsum_b.append(sum(comb))

subsum_a.sort()  # 이분 탐색을 위해 부분집합 합을 정렬
ans = 0  # 결과값 초기화

# 이분 탐색을 통해 가능한 경우의 수 찾기
for element_b in subsum_b:
    if element_b > c:  # 두 번째 그룹의 부분집합 합이 c를 넘으면 무시
        continue

    start = 0  # 이분 탐색을 위한 시작 인덱스
    end = len(subsum_a) - 1  # 이분 탐색을 위한 끝 인덱스

    while start <= end:
        mid = (start + end) // 2
        if subsum_a[mid] + element_b > c:  # 두 부분집합의 합이 c를 넘으면 탐색 범위를 줄임
            end = mid - 1
        else:  # 두 부분집합의 합이 c 이하이면 현재까지의 부분집합의 개수를 결과값에 더함
            start = mid + 1

    ans += end + 1

print(ans)  # 결과 출력
