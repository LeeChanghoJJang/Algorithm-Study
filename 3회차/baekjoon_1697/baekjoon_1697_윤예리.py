from collections import deque
sb, sis = map(int, input().split())

def bfs(start, end):
    # queue에 2개 정보 저장
    q = deque([[start, 0]]) # 시작 시간, 걸린 시간
    visited = []

    while q:
        now, sec = q.popleft()

        # if문 대신 while문 못쓰려나
        if now == end:      # 동생 잡으면 종료
            return sec
        next_ = [now-1, now+1, now*2] 
        for n in next_:
            if n not in visited:    # 계산 안 한 거리만
                visited.append(n)
                q.append([n, sec+1])    # 시간과 depth 저장
                                        # [4, 2], [6, 2], [10, 2]

print(bfs(sb, sis))

# dp로는 못 푸려나