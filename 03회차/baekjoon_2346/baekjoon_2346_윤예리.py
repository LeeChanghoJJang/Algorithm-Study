from collections import deque
N = int(input())
balloons = deque(enumerate(map(int, input().split())))  # 풍선 인덱스랑 안의 종이 내용을 같이 받아옴

while balloons:
    now, paper = balloons.popleft()
    print(now+1, end=' ')

    if not balloons:
        break

    if paper > 0:   # 오른쪽 이동
        for i in range(paper-1):
            a = balloons.popleft()  # 종이에 적힌 수 - 1 번 오른쪽에서 빼서 왼쪽에 넣는다.
            balloons.append(a)
    else:           # 왼쪽 이동
        for i in range(abs(paper)):
            a = balloons.pop()
            balloons.insert(0, a)
            
# 화덕 문제랑 비슷하게 풀었음

'''
# 풍선이 안 터지니까 index 계산이 어려움
# 반례
# 10
# 1 -2 3 -4 5 -6 7 -8 9 -10
# 
# 1 2 9 3 6 5 7 8 10 4

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
'''