N = int(input())

tree = {}
for _ in range(N):
    root, l, r = map(str, input().split())
    tree[root] = [l, r]


def preorder(i):
    if i == '.': return
    left, right = tree[i]

    print(i, end='')
    preorder(left)
    preorder(right)


def inorder(i):
    if i == '.': return
    left, right = tree[i]

    inorder(left)
    print(i, end='')
    inorder(right)


def postorder(i):
    if i == '.': return
    left, right = tree[i]

    postorder(left)
    postorder(right)
    print(i, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')