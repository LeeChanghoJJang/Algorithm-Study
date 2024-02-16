N = int(input())
balloons = list(map(int, input().split()))

visited = [0] * N
result = []
here = 0    # 풍선 인덱스
while len(result) < N:
    result.append(here+1)
    pop_ = balloons[here]   # 터진 풍선 안의 숫자
    visited[here] = 1

    if pop_ > 0:        # 오른쪽 이동
        if visited[(here+pop_)%N] == 0: # 터진적 없는 풍선이면
            here = (here+pop_)%N
        else:
            for i in range(N):   # 순회하면서 안 터진 풍선을 찾음
                if visited[i] == 0:
                    here = i
                    break

    else:               # 왼쪽 이동
        if visited[(here + pop_) % N] == 0:  # 터진적 없는 풍선이면
            here = (here + pop_) % N
        else:
            for i in range(N-1, -1, -1):  # 순회하면서 안 터진 풍선을 찾음
                if visited[i] == 0:
                    here = i
                    break
print(*result)