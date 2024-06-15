# N =int(input())
# n_lst = [[] for _ in range(8)]
# n_lst_for_sort = []

# result = 0
# alpha_dict = {}
# num = 9
# # n_lst에 자리에 맞는 알파벳 넣어놓고 숫자 배정
# # 숫자는 딕셔너리에. 없으면 알파벳:숫자 저장. 숫자는 어차피 순서대로라 key로 안해도 될듯.
# # 딕셔너리에 호출,저장하면서 result에 저장
# # 같은 자리에서도 뒤에 어디서 나오냐에 따라 우선순위 필요
# for _ in range(N):
#     tem  = input()
#     # 문자열
#     for t in range(len(tem)):
#         n_lst[8-len(tem)+t].append(tem[t])
        

#         for T in range(len(n_lst_for_sort)):
#             if tem[t] == n_lst_for_sort[T][1]:
#                 # tem[t]가 앞에 나왔냐 안나왔냐. n_lst_for_sort에 2번째 요소중에 나왔냐.
#                 n_lst_for_sort[T][0].append(8-len(tem)+t)
#                 n_lst_for_sort[T][0].sort()
#                 break
#         else:
#             n_lst_for_sort.append([[8-len(tem)+t],tem[t]])
#             # 지금 자리에 
# # 그럼 n_lst_for_sort에서 정렬한 대로 dict에 num 넣고 하면 될듯.

# n_lst_for_sort.sort()
# for tem_lst in n_lst_for_sort:
#     alpha_dict[tem_lst[1]] = num
#     num -= 1
# for i in range(8):
#     if n_lst[i]:
#         for alp in n_lst[i]:
#             result += alpha_dict[alp]*(10**(7-i))
#             # 값이 있으면 그냥 호출, 아니면 넣고 num -= 1

# print(result)
            
import sys
N = int(sys.stdin.readline())
S = [sys.stdin.readline().strip() for _ in range(N)]
words = {} # 단어별 값을 지정
for s in S: 
    x = len(s)-1 # 10의 제곱을 해줄 값
    for i in s :
        if i in words:
            words[i] += 10**x # 있으면 x만큼 제곱한걸 더하고
        else :
            words[i] = 10**x # 없으면 x만큼 제곱해서 넣자
        x -= 1

words_sort = sorted(words.values(),reverse=True) # 딕셔너리의 value만 내림차순으로 가져오자
result = 0
num = 9
for k in words_sort:
    result += k * num # 내림차순 한거에 9부터 하나씩 곱해서 더해주자
    num -= 1
print(result)
        
        
    