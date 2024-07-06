import math
import sys

sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
# in_range = lambda y,x: 0<=y<n and 0<=x<m

# 세그먼트 트리 노드 생성 함수
def make_seg(idx, s, e):

    if s == e:
        seg[idx] = (arr[s], arr[s])  # 현재 구간의 최솟값, 최댓값 저장
        return seg[idx]

    mid = (s + e) // 2

    # 왼쪽 자식 노드와 오른쪽 자식 노드 생성
    l = make_seg(idx * 2, s, mid)
    r = make_seg(idx * 2 + 1, mid + 1, e)

    # 현재 노드에 왼쪽 자식 노드와 오른쪽 자식 노드의 최솟값, 최댓값 저장
    seg[idx] = (min(l[0], r[0]), max(l[1], r[1]))
    return seg[idx]

# 특정 구간의 최솟값과 최댓값을 반환하는 함수
def f(s, e, idx):

    # 탐색 범위가 구간 [a, b]와 겹치지 않는 경우
    if e < a or b < s:
        return (1000000000, 0)  # 초기화된 매우 큰 값

    mid = (s + e) // 2

    # 탐색 범위가 현재 구간 [s, e]에 완전히 포함되는 경우
    if a <= s and e <= b:
        return seg[idx]  # 현재 구간의 최솟값과 최댓값 반환

    # 탐색 범위가 현재 구간을 일부만 포함하는 경우
    else:
        # 왼쪽 자식 노드와 오른쪽 자식 노드에서 탐색을 진행하여 결과를 얻음
        l = f(s, mid, idx * 2)
        r = f(mid + 1, e, idx * 2 + 1)
        # 왼쪽 자식 노드와 오른쪽 자식 노드의 결과 중에서 최솟값과 최댓값 반환
        return (min(l[0], r[0]), max(l[1], r[1]))


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]  # 입력값 저장

# 세그먼트 트리의 높이를 구함
b = math.ceil(math.log2(n)) + 1
# 세그먼트 트리의 노드 수 계산
node_n = 1 << b
# 세그먼트 트리 초기화
seg = [0 for _ in range(node_n)]
# 세그먼트 트리 생성
make_seg(1, 0, len(arr) - 1)

# 질의 수행
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1  # 0-based index로 변환
    # 특정 구간의 최솟값과 최댓값 출력
    ans = f(0, len(arr) - 1, 1)
    print(ans[0], ans[1])
