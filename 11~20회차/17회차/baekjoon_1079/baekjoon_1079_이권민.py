import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())
criminal = list(map(int, input().split()))

R = [
    list(map(int, input().split()))
    for _ in range(n)
]

eunjin = int(input())
is_alive = [True] * n

ans = 0
flag = False
def mafia(remain, nights):
    global ans, flag

    if flag:
        return

    ans = max(ans, nights)

    if remain == 0:
        return

    if remain == 1 and is_alive[eunjin]:
        flag = True
        return

    # 짝수명이 남았으면 밤이다.
    if remain % 2 == 0:
        for i in range(n):
            if not is_alive[i] or i == eunjin:
                continue
            is_alive[i] = False
            # 살아있는 사람들의 유죄 지수 변경
            for j in range(n):
                if not is_alive[j]:
                    continue
                criminal[j] += R[i][j]
            mafia(remain - 1, nights + 1)
            # 원상 복구
            for j in range(n):
                if not is_alive[j]:
                    continue
                criminal[j] -= R[i][j]
            is_alive[i] = True

    # 홀수명이 남았으면 낮이다.
    else:
        max_criminal = -1
        index = -1

        for i, c in enumerate(criminal):
            if not is_alive[i]:
                continue

            if max_criminal < c:
                index = i
                max_criminal = c

        if index == eunjin:
            return

        is_alive[index] = False
        mafia(remain - 1, nights)
        is_alive[index] = True

mafia(n, 0)

print(ans)