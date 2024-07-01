# 1991 트리 순회

N = int(input()); tree = {}

for i in range(N):  # 트리 제작
    P, L, R = input().split()
    tree[P] = [L, R]

def pre_order(now):  # 전위 순회
    if now == '.': return
    print(now, end='')
    pre_order(tree[now][0])
    pre_order(tree[now][1])

def in_order(now):  # 중위 순회
    if now == '.': return
    in_order(tree[now][0])
    print(now, end='')
    in_order(tree[now][1])

def post_order(now):  # 후위 순회
    if now == '.': return
    post_order(tree[now][0])
    post_order(tree[now][1])
    print(now, end='')

pre_order('A'); print()
in_order('A'); print()
post_order('A')