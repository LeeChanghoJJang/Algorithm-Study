from collections import deque
sb, sis = map(int, input().split())

def bfs(start, end):
    q = deque([[start, 0]]) # 시작 시간, 걸린 시간
    visited = []

    while q:
        now, sec = q.popleft()

        # while문 못쓰려나
        if now == end:
            return sec
        next_ = [now-1, now+1, now*2]
        for n in next_:
            if n not in visited:    # 계산 안 한 거리만
                visited.append(n)
                q.append([n, sec+1])

print(bfs(sb, sis))

# dp로는 못 푸려나