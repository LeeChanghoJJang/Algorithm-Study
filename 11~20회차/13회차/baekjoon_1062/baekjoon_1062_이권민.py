# # a c n t i 
# def BT(cur,cnt,n,k,result):
# # 슬라이싱 후 안에 글자 체크. K를 안넘어가면 추가.
# # 추가한거랑 안한거 두개 돌리기. 넣은 거 초기화.
# # if문으로 해서 가능하면.
#     global max_cnt
#     if cur == n:
#         max_cnt = max(result,max_cnt)
#         return
#     print(result)
#     check_st = st_lst[cur]
#     tem_cnt = cnt
#     plus_lst = []
#     for st in check_st:
#         if st not in "antic":
#             if alpha_lst[ord(st)-97] == 0:
#                 alpha_lst[ord(st)-97] = 1
#                 plus_lst.append(ord(st)-97)
#                 tem_cnt += 1
#             if tem_cnt > k:
#                 break
#     else:
#         BT(cur+1,tem_cnt,n,k,result+1)
#     for st_n in plus_lst:
#         alpha_lst[st_n] = 0
#     BT(cur+1,cnt,n,k,result)
        
            
    

# N, K = map(int,input().split())
# st_lst = [input() for _ in range(N)]
# alpha_lst = [0]*26
# alpha_lst[ord('a')-97] = 1
# alpha_lst[ord('n')-97] = 1
# alpha_lst[ord('t')-97] = 1
# alpha_lst[ord('c')-97] = 1
# alpha_lst[ord('i')-97] = 1
# max_cnt = 0
# if K <5:
#     print(0)
# else:
#     BT(0,5,N,K,0)
#     print(max_cnt)

import sys
from itertools import combinations

input = sys.stdin.readline

def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a'))
    return bit

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
bits = list(map(word2bit, words))
base_bit = word2bit('antic')

if K < 5:
    print(0)
else:
    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    answer = 0
    for combination in combinations(alphabet, K-5):
        know_bit = sum(combination) | base_bit
        count = 0
        for bit in bits:
            if bit & know_bit == bit:
                count += 1
        answer = max(answer, count)
    print(answer)