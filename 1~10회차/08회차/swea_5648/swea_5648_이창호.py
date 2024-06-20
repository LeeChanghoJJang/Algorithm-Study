import sys
sys.stdin = open('input.txt')

# 원자의 이동 방향을 정의하는 상수
# (오른쪽, 왼쪽, 위쪽, 아래쪽)
ways = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}

# 테스트 케이스 반복
for tc in range(1, int(input()) + 1):
    N = int(input())  # 원자의 개수

    # 원자 정보를 저장할 리스트
    wonja = []
    for _ in range(N):
        x, y, way, energy = map(int, input().split())
        # 위치를 2배로 확장
        x = 2 * x
        y = 2 * y
        f_time = 0  # 초기 시간
        wonja.append([x, y, way, energy, f_time])

    result = 0  # 원자들이 소멸될 때까지 충돌하여 방출되는 에너지의 총합
    # 원자들의 정보를 저장하는 딕셔너리
    # 키: (x, y) 좌표, 값: [원자 인덱스, 에너지량, 시간, 터져서 사라져야 할 여부(팡)]
    info = {}

    # 4004번까지 시뮬레이션 실행 (원자의 위치가 최대 -2000 ~ 2000까지 가능)
    for _ in range(4004):
        check = 0  # 원자들의 이동 여부를 체크하기 위한 변수
        # 원자들 이동
        for i in range(N):
            x, y, way, energy, time = wonja[i]
            time += 1  # 시간 증가
            check += (energy > 0)  # 에너지가 0보다 크면 check 증가
            pang = 0  # 원자의 충돌 여부
            if energy == 0:  # 에너지가 0인 경우는 이미 충돌하여 소멸된 상태
                continue

            nx = x + ways[way][0]  # 다음 x 좌표
            ny = y + ways[way][1]  # 다음 y 좌표
            # 좌표가 범위를 벗어나면 소멸됨
            if not (abs(nx) <= 2000 and abs(ny) <= 2000):
                wonja[i][3] = 0  # 에너지 0 처리
            # 딕셔너리에 다음 위치 정보 저장
            if (nx, ny) not in info.keys():
                info[(nx, ny)] = [i, energy, time, 0]
            else:
                # 충돌이 발생한 경우
                existing_num, existing_energy, existing_time, pang = info[(nx, ny)]
                if time == existing_time:  # 동시에 충돌한 경우
                    # 충돌한 원자들의 에너지 합쳐서 저장하고, 충돌 여부 저장
                    info[(nx, ny)] = [i, wonja[i][3] + existing_energy, time, 1]
                    # 충돌로 인해 소멸된 원자는 에너지를 0으로 설정
                    wonja[i][3] = 0
                    wonja[existing_num][3] = 0
            # 다음 좌표로 이동
            wonja[i][0], wonja[i][1], wonja[i][4] = nx, ny, time
            # 이전 위치 정보 삭제
            if info.get((x, y)):
                del info[(x, y)]

        # 충돌로 인한 에너지 합산
        for i in info.copy().keys():
            if info[i][-1]:  # 충돌 여부 체크
                result += info[i][1]  # 에너지 합산
                del info[i]  # 충돌로 인해 소멸된 원자 정보 삭제
        # 모든 원자가 이동을 마쳤을 때
        if check == 0:
            # 남아있는 원자들의 에너지를 합산하고 종료
            for i in info.keys():
                if abs(i[0]) <= 2000 and abs(i[1]) <= 2000:
                    result += info[i][1]
            break

    print(f'#{tc} {result}')  # 결과 출력
