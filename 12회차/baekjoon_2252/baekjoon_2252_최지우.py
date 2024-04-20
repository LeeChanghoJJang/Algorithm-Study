import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 정방향 순서
link = {i:[] for i in range(N+1)}
# 역방향 순서
rev_link = {i:[] for i in range(N+1)}
# _ => i로 오는 배열이 비어있다면, 줄에 넣어도 된다

# 먼저 다 넣어두고, B에 한 번이라도 나오면 뺄거임
start = {i for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())

    # 입력 받으면서 시작 불가능한 사람 뻄
    if b in start:
        start.remove(b)
    link[a].append(b)
    rev_link[b].append(a)

line = []

while start:
    # 현재 사람 줄에 세움
    v = start.pop()
    line.append(v)
    # 지금 사람을 줄에 세우고 나면 다음에 올 수 있는 사람 체크
    # 역방향 연결에서 지금 사람 빼고, 배열이 비면 줄에 세워도 됨
    for i in link[v]:
        rev_link[i].remove(v)
        if not rev_link[i]:
            start.add(i)
print(*line)
