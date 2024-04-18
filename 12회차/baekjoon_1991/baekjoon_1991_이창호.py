import sys

# 표준 입력을 'input.txt'에서 읽도록 재지정
sys.stdin = open('input.txt')

# 트리의 노드 수 입력
N = int(input())

# 전위 순회 함수
def preorder(now):
    if trees.get(now):  # 현재 노드에 자식이 있는 경우
        print(now, end='')  # 현재 노드 출력
        preorder(trees[now][0])  # 왼쪽 자식을 기준으로 재귀 호출
        preorder(trees[now][1])  # 오른쪽 자식을 기준으로 재귀 호출

# 중위 순회 함수
def inorder(now):
    if trees.get(now):  # 현재 노드에 자식이 있는 경우
        inorder(trees[now][0])  # 왼쪽 자식을 기준으로 재귀 호출
        print(now, end='')  # 현재 노드 출력
        inorder(trees[now][1])  # 오른쪽 자식을 기준으로 재귀 호출

# 후위 순회 함수
def postorder(now):
    if trees.get(now):  # 현재 노드에 자식이 있는 경우
        postorder(trees[now][0])  # 왼쪽 자식을 기준으로 재귀 호출
        postorder(trees[now][1])  # 오른쪽 자식을 기준으로 재귀 호출
        print(now, end='')  # 현재 노드 출력

# 트리 구성
trees = {}
for i in range(N):
    now, left, right = input().split()
    trees[now] = [left, right]

# 전위 순회 출력
preorder('A')
print()
# 중위 순회 출력
inorder('A')
print()
# 후위 순회 출력
postorder('A')
