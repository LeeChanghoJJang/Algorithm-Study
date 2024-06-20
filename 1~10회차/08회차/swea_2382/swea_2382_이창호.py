import sys
sys.stdin = open('input.txt')  # input.txt 파일을 입력으로 사용

from collections import deque

# 이동 방향에 따른 좌표 변화량을 정의
ways = {1: (-1, 0),  # 상
        2: (1, 0),   # 하
        3: (0, -1),  # 좌
        4: (0, 1)}   # 우

# 테스트 케이스 반복
for tc in range(1, int(input()) + 1):
    # 입력 받기
    N, M, K = map(int, input().split())  # N: 배열 크기, M: 시간, K: 미생물 군집 수
    arr = [[0] * N for _ in range(N)]    # N x N 배열 초기화
    temp = deque([])                     # 미생물 군집 정보를 담을 deque 초기화

    # 초기 미생물 군집 정보 입력
    for _ in range(K):
        x, y, cnt, way = map(int, input().split())
        temp.append([x, y, cnt, way])

    # 시간 M만큼 반복
    for _ in range(M):
        info = {}  # 각 위치에 대한 미생물 군집 정보를 담을 딕셔너리 초기화

        # 모든 미생물 군집에 대해 처리
        for i in range(K):
            x, y, cnt, way = temp[i]
            nx = x + ways[way][0]  # 다음 위치 계산
            ny = y + ways[way][1]

            temp[i][0], temp[i][1] = nx, ny  # 미생물 군집의 위치 갱신

            # 만약 다음 위치가 배열의 경계에 닿았을 경우
            if nx in [0, N - 1] or ny in [0, N - 1]:
                # 방향 변경 및 미생물 수 감소
                if way <= 2: way = 3 - way
                elif way <= 4: way = 7 - way
                cnt //= 2
                temp[i][2],temp[i][3] = cnt, way

            # info 딕셔너리에 해당 위치의 미생물 군집 정보 추가
            if (nx, ny) not in info.keys():
                info[(nx, ny)] = [i, cnt]
            else:
                num, max_cnt = info[(nx, ny)]
                # 미생물 수가 더 많은 군집이 이미 있을 경우
                if temp[i][2] > max_cnt:
                    info[(nx, ny)] = [i, cnt]  # 현재 군집 정보 갱신
                    temp[i][2] += temp[num][2]  # 더 많은 미생물 수를 가진 군집의 미생물 수 추가
                    temp[num][2] = 0  # 원래 군집의 미생물 수 초기화
                else:
                    temp[num][2] += temp[i][2]  # 이미 있는 군집에 미생물 수 추가
                    temp[i][2] = 0  # 현재 군집의 미생물 수 초기화

    # 결과 계산
    result = 0
    for i in range(len(temp)):
        result += temp[i][2]

    # 결과 출력
    print(f'#{tc} {result}')
