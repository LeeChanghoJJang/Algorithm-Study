# 10815 숫자 카드
# N개의 숫자 카드 / 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드가 있는지 없는지 판별
# print(*list(map(lambda x: int(x in N_card), M_card))) 로 하려고 했으나 시간 초과
# x in a : O(N) / map : O(M) / list(map(~)) : O(M) > O(N*M^2)의 시간 복잡도를 가짐
# 따라서 해시를 이용하여 탐색 시간을 줄이는 딕셔너리 사용 + 정수 키라 순서도 변경되지 않음

import sys

# 입력
N = int(sys.stdin.readline())
N_card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_card = {}
for i in list(map(int, sys.stdin.readline().split())):
    M_card[i] = 0

# 상근이가 가지고 있는 카드 순회
for num in N_card:
    # 카드가 딕셔너리의 키 목록에 있으면 1로 변경
    if num in M_card.keys():
        M_card[num] = 1

# 출력
print(*M_card.values())