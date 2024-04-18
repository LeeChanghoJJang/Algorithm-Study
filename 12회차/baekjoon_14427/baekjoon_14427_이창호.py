import sys
sys.stdin = open('input.txt')

# Segment Tree 초기화 함수
def init(start, end, index):
    # 만약 시작과 끝이 같으면 해당 위치의 값을 트리에 저장
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start + end) // 2
        # 좌측과 우측 자식으로 분할하여 재귀적으로 트리를 채움
        tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
    return tree[index]

# 값 갱신 함수
def update(start, end, index, w, v):
    # 범위를 벗어나는 경우에는 종료
    if w < start or w > end:
        return
    # 리프 노드에 도달한 경우
    if start == end:
        tree[index] = v
        return tree[index]
    mid = (start + end) // 2
    # 좌측과 우측 자식으로 분할하여 갱신 대상이 있는 쪽을 선택하여 재귀 호출
    update(start, mid, index * 2, w, v)
    update(mid + 1, end, index * 2 + 1, w, v)
    # 갱신된 자식 노드들 중에서 최소값을 부모 노드에 저장
    tree[index] = min(tree[index * 2], tree[index * 2 + 1])

# 최소값 찾기 함수
def find_min(start, end, index, left, right):
    # 범위를 벗어나는 경우 최대값 반환
    if start > right or end < left:
        return [sys.maxsize, sys.maxsize]
    # 범위가 완전히 속하는 경우 현재 노드의 값을 반환
    if start >= left and end <= right:
        return tree[index]
    mid = (start + end) // 2
    # 좌측과 우측 자식으로 분할하여 최소값을 찾음
    return min(find_min(start, mid, index * 2, left, right), find_min(mid + 1, end, index * 2 + 1, left, right))

# 입력 받기
N = int(input())
tmp = list(map(int, input().split()))
arr = []
for i in range(N):
    # (값, 인덱스) 형태로 리스트에 저장
    arr.append([tmp[i], i + 1])
tree = [0] * (N * 4)

# Segment Tree 초기화
init(0, N - 1, 1)

# 쿼리 처리
for j in range(int(input())):
    tmp = list(map(int, input().split()))
    if tmp[0] == 2:
        # 2번 쿼리인 경우 최소값 출력
        print(find_min(0, N - 1, 1, 0, N - 1)[1])
    elif tmp[0] == 1:
        # 1번 쿼리인 경우 값 갱신 및 트리 재구성
        arr[tmp[1] - 1][0] = tmp[2]
        update(0, N - 1, 1, tmp[1] - 1, arr[tmp[1] - 1])
