import sys, math

# 입력 받기
N = int(input())  # 배열의 크기
A_lst = [0] + list(map(int, input().split()))  # 초기 배열
M = int(input())  # 쿼리의 수

# 세그먼트 트리 초기화를 위한 노드의 개수 계산
node = math.ceil(math.log2(N))
node = 2 ** node

# 세그먼트 트리 초기화
tree = [[float('inf'), -1] for _ in range(node * 2)]

# 초기 배열 값을 세그먼트 트리에 저장
for i in range(N):
    treeNum = i + node
    tree[treeNum] = [A_lst[i], i]

# 세그먼트 트리 구축
for i in range(node - 1, 0, -1):
    left, right = tree[2 * i], tree[(2 * i) + 1]
    if left[0] <= right[0]:
        tree[i] = [left[0], left[1]]
    else:
        tree[i] = [right[0], right[1]]

# 값 업데이트 함수 정의
def update(idx, value):
    treeNum = idx + node
    tree[treeNum][0] = value
    while treeNum != 1:
        treeNum = treeNum // 2
        left, right = tree[2 * treeNum], tree[(2 * treeNum) + 1]
        if left[0] <= right[0]:
            tree[treeNum] = [left[0], left[1]]
        else:
            tree[treeNum] = [right[0], right[1]]

# 쿼리 처리
for _ in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:  # 쿼리가 1인 경우
        print(tree[1][1] + 1)  # 최솟값을 가진 인덱스 출력
    else:  # 쿼리가 2인 경우
        update(query[1], query[2])  # 값 업데이트

        
        
