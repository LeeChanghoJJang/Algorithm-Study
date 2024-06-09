import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
ej = int(input())
is_alive = [True] * n

result = 0
flag = False
def mafia(people, days):
    global result, flag, is_alive

    if flag:
        return
    result = max(result, days)
    if people == 0:
        return
    if people == 1 and is_alive[ej]:
        flag = True
        return

    # 밤
    if not people % 2:
        for i in range(n):
            if not is_alive[i] or i == ej:
                continue

            # dfs
            is_alive[i] = False
            for j in range(n):
                if not is_alive[j]:
                    continue
                score[j] += arr[i][j]
            mafia(people-1, days+1)
            for j in range(n):
                if not is_alive[j]:
                    continue
                score[j] -= arr[i][j]
            is_alive[i] = True

    # 낮
    else:
        max_score = -1
        idx = -1

        for i, c in enumerate(score):
            if not is_alive[i]:
                continue

            if max_score < c:
                idx = i
                max_score = c

        if idx == ej:
            return

        is_alive[idx] = False
        mafia(people-1, days)
        is_alive[idx] = True

mafia(n, 0)
print(result)