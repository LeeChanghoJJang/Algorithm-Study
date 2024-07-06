import sys


input = sys.stdin.readline


def preorder(root="A"):
    if root != '.':
        print(root, end="")
        preorder(graph[root][0])
        preorder(graph[root][1])


def inorder(root="A"):
    if root != '.':
        inorder(graph[root][0])
        print(root, end="")
        inorder(graph[root][1])


def postorder(root="A"):
    if root != '.':
        postorder(graph[root][0])
        postorder(graph[root][1])
        print(root, end="")


N = int(input())

graph = dict()
for _ in range(N):
    a,b,c = input().split()
    graph[a] = [b,c]


preorder()
print()
inorder()
print()
postorder()