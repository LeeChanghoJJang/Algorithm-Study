import sys
sys.stdin = open('input.txt')  # 표준 입력을 파일로 변경

T = int(input())  # 테스트 케이스 수 입력

for tc in range(T):
    N = int(input())  # 격자의 크기 입력
    atom_dict = {}  # 원자 정보를 저장할 딕셔너리
    visited = set()  # 충돌한 원자의 위치를 저장할 집합
    result = 0  # 결과 변수 초기화

    # 원자 정보 입력 및 딕셔너리에 저장
    for _ in range(N):
        x, y, d, e = map(int, input().split())
        atom_dict[-y, x] = (e, d)

    # 충돌 시뮬레이션
    for atom1 in atom_dict:
        e, d = atom_dict[atom1]
        temp = []  # 충돌할 수 있는 원자들을 저장할 임시 리스트

        # 모든 원자에 대해 충돌 확인
        for atom2 in atom_dict:
            if atom1 == atom2 or d == atom_dict[atom2][1]:  # 같은 원자거나 같은 방향으로 이동하는 경우 제외
                continue

            # 충돌 조건에 따라 temp에 추가
            if d == 0:  # 상 방향으로 이동하는 경우
                if atom1[0] < atom2[0]:
                    continue
                if atom_dict[atom2][1] == 1 and atom1[1] == atom2[1]:
                    temp.append(((atom1[0] - atom2[0]) / 2, atom2))
                elif atom_dict[atom2][1] == 2 and atom2[0] - atom1[0] == atom1[1] - atom2[1]:
                    temp.append((atom1[0] - atom2[0], atom2))
                elif atom_dict[atom2][1] == 3 and atom2[0] - atom1[0] == atom2[1] - atom1[1]:
                    temp.append((atom1[0] - atom2[0], atom2))
            elif d == 1:  # 하 방향으로 이동하는 경우
                if atom1[0] > atom2[0]:
                    continue
                if atom_dict[atom2][1] == 0 and atom1[1] == atom2[1]:
                    temp.append(((atom2[0] - atom1[0]) / 2, atom2))
                elif atom_dict[atom2][1] == 2 and atom2[0] - atom1[0] == atom2[1] - atom1[1]:
                    temp.append((atom2[0] - atom1[0], atom2))
                elif atom_dict[atom2][1] == 3 and atom2[0] - atom1[0] == atom1[1] - atom2[1]:
                    temp.append((atom2[0] - atom1[0], atom2))
            elif d == 2:  # 좌 방향으로 이동하는 경우
                if atom1[1] < atom2[1]:
                    continue
                if atom_dict[atom2][1] == 3 and atom1[0] == atom2[0]:
                    temp.append(((atom1[1] - atom2[1]) / 2, atom2))
                elif atom_dict[atom2][1] == 0 and atom2[0] - atom1[0] == atom1[1] - atom2[1]:
                    temp.append((atom1[1] - atom2[1], atom2))
                elif atom_dict[atom2][1] == 1 and atom2[0] - atom1[0] == atom2[1] - atom1[1]:
                    temp.append((atom1[1] - atom2[1], atom2))
            elif d == 3:  # 우 방향으로 이동하는 경우
                if atom1[1] > atom2[1]:
                    continue
                if atom_dict[atom2][1] == 2 and atom1[1] == atom2[1]:
                    temp.append(((atom2[1] - atom1[1]) / 2, atom2))
                elif atom_dict[atom2][1] == 0 and atom2[0] - atom1[0] == atom2[1] - atom1[1]:
                    temp.append((atom2[1] - atom1[1], atom2))
                elif atom_dict[atom2][1] == 1 and atom2[0] - atom1[0] == atom1[1] - atom2[1]:
                    temp.append((atom2[1] - atom1[1], atom2))

            # 충돌이 발생한 경우 temp를 정렬하여 stack에 저장
            if temp:
                temp.sort()
                stack = {}  # 충돌 시간을 키로, 충돌한 원자 정보를 값으로 가지는 딕셔너리

                # 충돌 시간별로 원자 정보를 저장
                for elem in temp:
                    if elem[0] in stack:
                        stack[elem[0]].add((elem[1], atom_dict[elem[1]][0]))
                    else:
                        stack[elem[0]] = {(elem[1], atom_dict[elem[1]][0])}

                # 충돌 시간별로 충돌한 원자들의 에너지 계산
                for time_ in stack:
                    len_ = sum(1 for e in stack for set_ in stack[e] if set_[0] not in visited)
                    for i in stack[time_]:
                        if i[0] not in visited:
                            result += i[1]
                            visited.add(i[0])

    print(f'#{tc + 1} {result}')  # 결과 출력