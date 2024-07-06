import sys
sys.stdin = open('input.txt')
'''
세그먼트 트리란?
-> 어떤 데이터가 존재할 때, 특정 구간의 결과값을 구하는데 사용하는 자료구조
- 장점 : 빠르다(단순 누적합일 때 O(N)인 반면, 최악일 때 O(NlogN) / 단점 : 메모리 많이 듦
1. 이진 트리 자료구조를 활용하여 각 초기값을 설정한다.
    - init함수는 리프노드일 경우에는 그 인덱스에 매칭되는 수 자체를 반환한다.
    - 점차 올라가면서 두 자식노드 간의 최소값을 부모노드에 저장한다.
2. 값을 갱신하면 그 노드부터 부모노드에 이르기까지 영향을 미치기 때문에 전부 변경이 필요하다.
ex) 5 4 3 2 1에 init 함수 실행시 tree는
[0, [1, 5], [3, 3], [1, 5], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

3. 최솟값을 찾는 함수는 find_min 함수이며, 트리 내의 최소값을 반환한다.
4. update함수는 현재 노드부터 루트노드까지 갱신할값 인덱스와 새값을 넣으면 그렇게 갱신해준다. 
'''
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
print(tree)
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
