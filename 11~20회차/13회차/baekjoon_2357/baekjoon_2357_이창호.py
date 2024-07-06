import sys
import math
sys.stdin = open('input.txt')

# make_seg : 세그먼트 트리를 만드는 함수
# 각 노드의 첫번째는 자식노드들의 최솟값, 두번째는 최댓값이 저장됨
# 루트 노드에는 범위를 최대화하고, 자식노드로 갈수록 범위는 좁아진다.
# 리프 노드에 도달할 경우, 그 인덱스에 해당하는 integer의 값을 반환한다.
def make_seg(start,end,index):
    if start == end:
        trees[index] = (integers[start],integers[start])
        return trees[index]
    mid = (start + end) // 2

    left_node = make_seg(start,mid,index*2)
    right_node = make_seg(mid+1,end,index*2+1)

    trees[index] = (min(left_node[0],right_node[0]),max(left_node[1],right_node[1]))
    return trees[index]
# 주어진 범위에 따른 최댓값과 최솟값을 반환하는 함수
def find(start,end,index):
    # 문제에서 주어진 범위에서 완전히 벗어난 경우
    if start > range2 or end < range1:
        return (sys.maxsize, 0)
    # 양쪽 끝이 범위 내에 들어온다면 tree의 index를 반환
    if start >= range1 and end <= range2:
        return trees[index]
    # 만약 한쪽 노드가 범위 밖이라면?
    # 범위 안쪽인 노드쪽에서의 최소, 최댓값만 도출해야함
    mid = (start + end) // 2
    left = find(start,mid,index*2)
    right = find(mid+1,end,index*2+1)
    return (min(left[0],right[0]),max(left[1],right[1]))

N,M = map(int,input().split())
integers = [int(input()) for _ in range(N)]
b = math.ceil(math.log2(N)) +1
node_n = 1 << b
trees = [0 for _ in range(node_n)]
make_seg(0,N-1,1)

for i in range(M):
    range1,range2 = map(int,input().split())
    range1 -= 1;range2 -= 1
    result = find(0,N-1,1)
    print(result[0],result[1])

