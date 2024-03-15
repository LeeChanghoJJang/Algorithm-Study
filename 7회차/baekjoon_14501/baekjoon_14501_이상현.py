from collections import deque

def bfs():
    global max_

    q = deque()
    q.append((0, 0))

    while q:
        day, money = q.popleft()

        if day < N:
            if day + list_[day][0] >= N:
                if day + list_[day][0] == N:
                    max_ = max(max_, money + list_[day][1])
                    q.append((day + 1, money))
                else:
                    max_ = max(max_, money)
                    q.append((day + 1, money))
            else:
                q.append((day + list_[day][0], money + list_[day][1]))
                q.append((day + 1, money))

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
max_ = 0
bfs()
print(max_)