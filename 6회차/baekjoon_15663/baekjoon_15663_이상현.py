# 백준 15663번 N과 M (9)

from itertools import permutations

_, M = map(int, input().split())
num_list = sorted(map(int, input().split()))

# 중복을 제거하기 위해 집합 이용
# 순열 라이브러리를 이용하여 num_list의 원소를
# 이용하여 만들 수 있는 모든 순열들의 리스트 생성
result = set()
list_ = list(permutations(num_list, M))
[result.add(elem) for elem in list_]

# 사전 순으로 증가하는 순서로 출력
[print(*elem) for elem in sorted(result)]