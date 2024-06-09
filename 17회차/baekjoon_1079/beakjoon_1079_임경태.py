# 1079 마피아

N = int(input())
F = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
E = int(input())

ans = 0
is_alive = [True] * N

def mafia(alive, night):
    global ans

    ans = max(ans, night)

    if alive == 1 and is_alive[E]:
        exit(print(ans))

    if alive == 0:
        return

    # 밤
    if alive % 2 == 0:
        for user in range(N):
            if not is_alive[user] or user == E:
                continue

            # 살아있는 사람들의 유죄 지수 변경
            is_alive[user] = False
            for other in range(N):
                if not is_alive[other]:
                    continue
                F[other] += R[user][other]

            mafia(alive - 1, night + 1)

            for other in range(N):
                if not is_alive[other]:
                    continue
                F[other] -= R[user][other]
            is_alive[user] = True

    # 낮
    else:
        max_criminal = user = -1

        for i, c in enumerate(F):
            if not is_alive[i]:
                continue

            if max_criminal < c:
                max_criminal = c
                user = i

        if user == E:
            return

        is_alive[user] = False
        mafia(alive - 1, night)
        is_alive[user] = True


mafia(N, 0)

print(ans)
