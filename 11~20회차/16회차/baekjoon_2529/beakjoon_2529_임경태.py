# 2529 부등호

k = int(input())
symbol = input().split()

min_val = 10e+10
max_val = 0
visit = [0] * 10

def DFS(idx, val, visit):
    global min_val
    global max_val

    if val: val = int(val)

    # 종료 조건 : 한계 깊이에 다다랐을때
    if idx >= k:
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        return

    for i in range(10):
        # 부등호에 따라 결정
        if symbol[idx] == '<' and val % 10 > i:
            continue
        if symbol[idx] == '>' and val % 10 < i:
            continue

        # 겹치지 않는 숫자 결정 
        if not visit[i]:
            visit[i] = 1
            DFS(idx + 1, str(val) + str(i), visit)
            visit[i] = 0

# 첫 숫자 선택
for i in range(10):
    visit[i] = 1
    DFS(0, f'{i}', visit)
    visit[i] = 0

if len(str(max_val)) < k+1:
    max_val = '0' + str(max_val)
print(max_val)

if len(str(min_val)) < k+1:
    min_val = '0' + str(min_val)
print(min_val)