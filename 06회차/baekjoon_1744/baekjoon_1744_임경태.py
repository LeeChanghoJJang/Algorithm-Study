# 1744 수묶기

N, pos, neg, ans = int(input()), [], [], 0

for _ in range(N):
    n = int(input())
    if n > 1: pos.append(n)
    elif n < 1: neg.append(n)
    else: ans += 1

pos.sort(reverse=True); neg.sort()  # 절댓값이 큰 수 부터 정렬

def f(pn):
    global ans
    for i in range(0, len(pn), 2):
        if len(pn) <= i+1: ans += pn[i]
        else: ans += pn[i] * pn[i+1]

f(pos); f(neg); print(ans)

'''
31120KB / 40ms
'''