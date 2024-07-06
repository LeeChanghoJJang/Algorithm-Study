import sys
input = sys.stdin.readline


# merge: 왼쪽 자식 노드, 오른쪽 자식 노드의 인덱스를 인자로 받아
# A[l], A[r] 비교 후 더 작은 값을 갖는 인덱스를 반환
# 세그먼트 트리에는 실제 수열의 값이 아닌, 작은 값을 갖는 인덱스가 저장됨.
def merge(l, r):
    if A[l] <= A[r]:
        return l
    return r


# 최초 트리 구현
# 1번 노드부터, start = 0, end = N-1
def maketree(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]

    mid = (start+end) // 2
    left = maketree(node*2, start, mid)
    right = maketree(node*2+1, mid+1, end)

    tree[node] = merge(left, right)
    return tree[node]


# 수열의 target 인덱스에 위치한 값을 new 로 변경
# 세그먼트 트리
# 루트 노드: 수열의 start ~ end 까지 값 중 최소값의 인덱스 저장
# 왼쪽 자식 노드: start ~ 부모노드//2 까지 최소값의 인덱스 저장
# 오른쪽 자식 노드: 부모노드//2+1 ~ end 까지 최소값 인덱스 저장
# node = 1, start = 0, end = N-1 부터 시작
def update(target, new, node, start, end):
    # 목표 인덱스가 start ~ end 범위에서 벗어나면
    # 변경하지 않고 현재 노드 값 그대로 반환
    if target < start or target > end:
        return tree[node]

    # 위 조건을 지나서 start==end: == target 에 도착
    # A[target] new 로 갱신 후 노드 값 반환
    if start == end:
        A[target] = new
        return tree[node]

    # 세그먼트 트리 이분탐색
    mid = (start+end) // 2
    left = update(target, new, node*2, start, mid)
    right = update(target, new, node*2+1, mid+1, end)

    # 두 자식노드 비교 후 merge 진행
    tree[node] = merge(left, right)
    return tree[node]


N = int(input())
A = list(map(int, input().split()))
M = int(input())

tree = [-1] * (4*N)
maketree(1, 0, N-1)

for _ in range(M):
    q, *etc = list(map(int, input().split()))
    if q == 1:
        i, v = etc
        update(i-1, v, 1, 0, N-1)
    else:
        print(tree[1]+1)

