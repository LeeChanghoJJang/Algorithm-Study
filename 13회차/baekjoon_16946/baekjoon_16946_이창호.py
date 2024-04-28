import sys
from collections import deque

# 입력 파일을 열어서 stdin으로 설정합니다.
sys.stdin = open('input.txt')

# 상하좌우 이동을 위한 변수를 설정합니다.
dr = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# 1로 둘러싸여 있는 0들의 그룹을 지정한다.
# group_dict에 각 무리의 정보를 저장해놓는다.
def grouping(x, y, num):
    # BFS를 위한 큐를 초기화합니다.
    queue = deque([[x, y]])
    # 해당 그룹의 번호를 부여하고, 해당 위치를 방문했음을 표시합니다.
    zeros[x][y] = num
    # 해당 그룹의 크기를 세기 위한 변수를 초기화합니다.
    cnt = 1
    # BFS 탐색을 시작합니다.
    while queue:
        x, y = queue.popleft()
        # 상하좌우 탐색을 수행합니다.
        for i in range(4):
            nx = x + dr[i][0]
            ny = y + dr[i][1]
            # 배열 범위 내에 있고, 블록이 0이고, 방문하지 않은 위치인 경우
            if 0 <= nx < N and 0 <= ny < M and not blocks[nx][ny] and not zeros[nx][ny]:
                # 해당 위치를 현재 그룹으로 표시하고, 큐에 추가합니다.
                zeros[nx][ny] = num
                queue.append([nx, ny])
                # 그룹의 크기를 1 증가시킵니다.
                cnt += 1
    return cnt

# 입력을 받습니다.
N, M = map(int, input().split())
blocks = [list(map(int, list(input().strip()))) for _ in range(N)]
zeros = [[0] * M for _ in range(N)]

# 각 0들이 모여있는 그룹의 크기를 저장할 딕셔너리를 초기화합니다.
group_dict = {}

# 그룹의 번호를 나누는 작업을 수행합니다.
num = 0
for i in range(N):
    for j in range(M):
        # 블록이 0이고, 방문하지 않은 위치인 경우에 대해서만 그룹을 나눕니다.
        if not blocks[i][j] and not zeros[i][j]:
            num += 1
            # 그룹의 번호를 key로, 그룹의 크기를 value로 저장해서,
            # 나중에 인접한 곳의 번호에 해당하는 값만 더해주면 되게끔
            group_dict[num] = grouping(i, j, num)

# 변환된 결과를 저장할 리스트를 초기화합니다.
output = []
# 각 위치를 순회하며 변환을 수행합니다.
for i in range(N):
    result = ''
    # temp : 각 위치별 연결된 0의 갯수를 저장하는 임시 변수
    for j in range(M):
        temp = 0
        # 블록이 1인 경우, 주변의 그룹에 대해 크기를 확인하고 결과를 계산합니다.
        if blocks[i][j]:
            # breaks에 넣는 이유는 같은 무리면 패스하게끔 해서 중복되게 저장하지 않으려고
            breaks = set()
            temp += 1
            # 인접한 상하좌우만 탐색해서 그 그룹의 0의 개수만 더해주면 됨
            for k in range(4):
                ni = i + dr[k][0]
                nj = j + dr[k][1]
                if 0 <= ni < N and 0 <= nj < M and not blocks[ni][nj] and zeros[ni][nj] and zeros[ni][nj] not in breaks:
                    breaks.add(zeros[ni][nj])
                    temp += group_dict[zeros[ni][nj]]
        # 결과를 10으로 나눈 나머지를 계산하여 문자열에 추가합니다.
        temp %= 10
        result += str(temp)
    # 한 행의 결과를 저장합니다.
    output.append(result)

# 결과를 출력합니다.
sys.stdout.write('\n'.join(output))
