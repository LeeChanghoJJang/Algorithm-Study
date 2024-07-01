N = int(input())
score = list(map(int, input().split()))
temp = tuple(tuple(map(int, input().split())) for _ in range(N))
player = int(input())
max_ = 1 << N
qq = [1 << i for i in range(N)]
vote = [[] for _ in range(max_)]
alive = [True] * N


def dfs(cur):
    cnt = 0
    killed = False
    for i in range(N):
        if not alive[i] or i == player:
            continue

        alive[i] = False
        nxt = cur | qq[i]

        for v in vote[nxt]:
            if v == player: break

            if alive[v]:
                alive[v] = False
                cnt = max(cnt, dfs(nxt))
                alive[v] = True
                break

        killed = alive[i] = True

    return cnt + 1 if killed else 0


def solve():
    for i in range(max_):
        died = [j for j in range(N) if i & qq[j]]
        vot = [(score[j] + sum(temp[k][j] for k in died), -j) for j in range(N) if i & qq[j] == 0]
        vot.sort(reverse=True)
        vote[i] = [-j for _, j in vot]

    if N % 2:
        if vote[0][0] == player:
            return 0
        alive[vote[0][0]] = False

    return dfs(0)

print(solve())