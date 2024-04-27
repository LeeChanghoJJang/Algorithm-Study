import sys
sys.stdin = open('input.txt')
# 첫번째 방법
# temp = []
# for i in range(9):
#     temp.append(int(input()))
#
# for i in range(1<<9):
#     result = []
#     for j in range(9):
#         if i&(1<<j):
#             result.append(temp[j])
#     if len(result)==7 and sum(result)==100:
#         break
#
# for i in sorted(result):
#     print(i)
# 두번째 방법
# temp = []
# for i in range(9):
#     temp.append(int(input()))
# def backtracking(start,result):
#     global min_val
#     if len(result)==7:
#         if sum(result) == 100:
#             min_val = sorted(result)
#             return
#
#     for i in range(start,9):
#         if not visited[i]:
#             visited[i]=1
#             result.append(temp[i])
#             backtracking(start+1,result)
#             result.pop()
#             visited[i] = 0
#
# visited = [0] * 10
# min_val = []
# backtracking(0,[])
# for i in range(len(min_val)):
#     print(min_val[i])
# 세번째 방법
sys.setrecursionlimit(10**6)
temp = []
for i in range(9):
    temp.append(int(input()))
def backtracking(start,result):
    global min_val
    global cnt
    cnt+=1
    if start < 9:
        print(result)
        print(cnt)
        if len(result)==7 and sum(result) == 100:
            min_val = sorted(result)
            return
        backtracking(start + 1, result)
        backtracking(start + 1, result+[temp[start]])

visited = [0] * 10
min_val = []
cnt=0
backtracking(0,[])
if min_val:
    for i in range(len(min_val)):
        print(min_val[i])

