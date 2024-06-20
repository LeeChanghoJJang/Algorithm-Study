# def chk(str1, str2):
#     for i in range(M):
#         if str1[i] == '.' or str2[i] == '.':
#             continue
#         if str1[i] != str2[i]:
#             return True
#     return False

# N, M = map(int, input().split())
# list_ = [input() for _ in range(N)]
# result = set()

# for str_ in list_:
#     if not result:
#         result.add(str_)
#     else:
#         if all(chk(str_, elem) for elem in result):
#             result.add(str_)

# print(len(result))

# gg