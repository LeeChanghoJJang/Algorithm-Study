# 14427 수열과 쿼리 15

# lazy propagation (느린 갱신) : 336ms
from heapq import heappush, heappop, heapify

n = int(input())
arr = [0] + list(map(int, input().split()))

Q = [(arr[i], i) for i in range(1, n+1)]
heapify(Q)

for _ in range(int(input())):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, v = query[1], query[2]
        arr[i] = v  # 갱신
        heappush(Q, (v, i))  # 추가
    else:
        # 맞는 값이 나올 때까지 제거
        while Q and arr[Q[0][1]] != Q[0][0]:
            heappop(Q)
        print(Q[0][1])  # 출력



# segment tree (세그먼트 트리) : 816ms

def init(left, right, index):
    # 범위 내에 하나의 요소만 있는 경우, 해당 요소를 트리 노드에 저장
    if left == right:
        tree[index] = arr[left]
    # 현재 노드의 왼쪽과 오른쪽 자식을 재귀적으로 초기화
    else:
        mid = (left + right) // 2
        tree[index] = min(init(left, mid, index*2), init(mid+1, right, index*2+1))
    return tree[index]

def update(start, end, index, w, v):
    # 업데이트할 인덱스가 현재 범위를 벗어난 경우, 반환
    if w < start or w > end:
        return
    # 현재 노드가 업데이트할 인덱스를 나타내는 경우, 값을 업데이트
    if start == end:
        tree[index] = v
        return tree[index]
    mid = (start+end) // 2
    # 현재 노드의 왼쪽과 오른쪽 자식을 재귀적으로 업데이트
    update(start, mid, index*2, w, v)
    update(mid+1, end, index*2+1, w, v)
    # 현재 노드의 값을 자식들의 값에 기반하여 업데이트
    tree[index] = min(tree[index*2], tree[index*2+1])

def find_min(start, end, index):
    # 범위가 배열을 완전히 벗어난 경우, 최대값을 반환
    if start > N-1 or end < 0:
        return [float('inf'), float('inf')]
    # 범위가 현재 노드가 나타내는 범위에 완전히 포함된 경우, 노드의 값 반환
    if start >= 0 and end <= N-1:
        return tree[index]
    mid = (start + end) // 2
    # 자식 노드에서 최솟값 검색
    return min(find_min(start, mid, index*2), find_min(mid+1, end, index*2+1))


N = int(input())
arr = [[n, i+1] for i, n in enumerate(map(int, input().split()))]
tree = [0] * (N*4)
init(0, N-1, 1)  # 세그먼트 트리 초기화

# 각 쿼리를 처리
for j in range(int(input())):
    query = list(map(int, input().split()))

    # 쿼리 타입이 1인 경우, 배열 및 세그먼트 트리 업데이트
    if query[0] == 1:
        arr[query[1]-1][0] = query[2]
        update(0, N-1, 1, query[1]-1, arr[query[1]-1])

    # 쿼리 타입이 2인 경우, 배열에서 최솟값의 인덱스를 출력
    elif query[0] == 2:
        print(find_min(0, N-1, 1)[1])