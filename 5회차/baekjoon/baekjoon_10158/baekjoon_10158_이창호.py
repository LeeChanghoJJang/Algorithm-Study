import sys
sys.stdin = open('input.txt')
# 첫번째 방법
# def movement(p,q,t):
#     cnt_0 = 1
#     cnt_1 = 1
#     while t>0:
#         if p == w or p==0:
#             cnt_0 = cnt_0 * (-1)
#         if q == h or q==0:
#             cnt_1 = cnt_1 * (-1)
#         p += cnt_0
#         q += cnt_1
#         t-=1
#     return p,q
#
# w,h = map(int,sys.stdin.readline().split())
# p,q = map(int,sys.stdin.readline().split())
# t = int(sys.stdin.readline())
# p,q=movement(p,q,t)
# print(p,q)
# 두번째 방법
# def movement(p,q,t):
#     cnt_0 = 1
#     cnt_1 = 1
#     while t>0:
#         if p == w or p==0:
#             cnt_0 = cnt_0 * (-1)
#         if q == h or q==0:
#             cnt_1 = cnt_1 * (-1)
#         if cnt_0 == -1:
#             if cnt_1 == -1:
#                 move = min(p,q)
#             elif cnt_1 ==1:
#                 move = min(p,abs(h-q))
#         elif cnt_0 == 1:
#             if cnt_1 == -1:
#                 move = min(abs(w-p), q)
#             elif cnt_1 == 1:
#                 move = min(abs(w-p), abs(h - q))
#
#         if t> move:
#             p += cnt_0 * move
#             q += cnt_1 * move
#             t-= move
#         else:
#             while t:
#                 p += cnt_0
#                 q += cnt_1
#                 t -= 1
#     return p,q
#
# w,h = map(int,input().split())
# p,q = map(int,input().split())
# t = int(input())
# p,q=movement(p,q,t)
# print(p,q)
# # 세번째 방법
# def movement(p, q, t, w, h):
#     cnt_0, cnt_1 = 1, 1
#
#     while t > 0:
#         move_0 = min(p, w - p) if cnt_0 == -1 else min(abs(w - p), p)
#         move_1 = min(q, h - q) if cnt_1 == -1 else min(abs(h - q), q)
#         move = min(move_0, move_1)
#
#         if t > move:
#             p += cnt_0 * move
#             q += cnt_1 * move
#             t -= move
#         else:
#             p += cnt_0 * t
#             q += cnt_1 * t
#             t = 0
#
#         cnt_0 *= -1 if p in {0, w} else 1
#         cnt_1 *= -1 if q in {0, h} else 1
#
#     return p, q
#
# w, h = map(int, input().split())
# p, q = map(int, input().split())
# t = int(input())
# p, q = movement(p, q, t, w, h)
# print(p, q)

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = (p + t) // w  # 증가하는 부분인지 감소하는 부분인지 확인
b = (q + t) // h  # 증가하는 부분인지 감소하는 부분인지 확인

if a % 2 == 0:  # 해당 값이 증가하는 부분이라면
    x = (p + t) % w
else:  # 해당 값이 감소하는 부분이라면
    x = w - (p + t) % w

if b % 2 == 0:  # 해당 값이 감소하는 부분이라면
    y = (q + t) % h
else:  # 해당 값이 감소하는 부분이라면
    y = h - (q + t) % h

print(x, y)