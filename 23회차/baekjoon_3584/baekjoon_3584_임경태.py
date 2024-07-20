# 3584 가장 가까운 공통 조상
for _ in range(int(input())):
    N = int(input())
    tree = {}

    for j in range(N - 1):
        a, b = map(int, input().split())
        tree[b] = a
    a, b = map(int, input().split())

    # a의 루트 노드들을 집합에 저장
    a_roots = set()
    while a in tree:
        a_roots.add(a)
        a = tree[a]
    a_roots.add(a)

    # b의 루트 노드로 올라가며 a의 루트 노드 집합에 있는지 확인
    while b not in a_roots:
        b = tree[b]

    print(b)
