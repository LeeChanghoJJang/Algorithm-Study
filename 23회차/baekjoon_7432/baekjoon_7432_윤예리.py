import sys
input = sys.stdin.readline

n = int(input())
child = dict()

def dfs(arr, d):
    for x in sorted(arr.keys()):
        print(' ' * d + x)
        dfs(arr[x], d+1)

for _ in range(n):
    lst = input().strip().split('\\')

    tmp = child

    for x in lst:
        if x not in tmp:
            tmp[x] = {}
        tmp = tmp[x]

dfs(child, 0)
# print(child)

# 메모리 초과
# n = int(input())
#
# child = dict()
# nodes = []
#
# def findRoot(x):
#     for i in child:
#         if x in child[i]:
#             return findRoot(i)
#     else:
#         if not x in roots:
#             roots.append(x)
#     return
#
# def findChild(x, space):
#     print(space+x)
#
#     if x in child:
#         for i in sorted(child[x]):
#             findChild(i, space+" ")
#     else:
#         return
#
# for _ in range(n):
#     tmp = input().split('\\')
#
#     nodes.extend(tmp)
#
#     for i in range(len(tmp)-1):
#         if tmp[i] not in child:
#             child[tmp[i]] = []
#
#         if tmp[i+1] not in child[tmp[i]]:
#             child[tmp[i]].append(tmp[i+1])
#
# nodes = list(set(nodes))
# roots = []
# # print(child)
# for x in nodes:
#     findRoot(x)
# for y in sorted(roots):
#     findChild(y, '')

