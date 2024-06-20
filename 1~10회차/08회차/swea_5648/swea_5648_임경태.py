# 5648 원자 소멸 시뮬레이션

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
 
for tc in range(int(input())):
    atoms = []
    for _ in range(int(input())):
        x, y, d, e = map(int, input().split())
        atoms.append([2*x, 2*y, d, e])
    ans = 0

    # 시간 경과
    while len(atoms) > 1:
        pos = {}
        # 위치 이동
        for atom in atoms:
            atom[0] += dx[atom[2]]
            atom[1] += dy[atom[2]]
            # 위치 저장
            if (atom[0], atom[1]) in pos: pos[(atom[0], atom[1])].append(atom)
            else:  pos[(atom[0], atom[1])] = [atom]

        for key, value in pos.items():
            # 배열 이탈
            if not (-2001 < key[0] < 2001 and -2001 < key[1] < 2001):
                atoms.remove(value.pop())
            # 충돌 소멸
            elif len(value) > 1:
                for atom in value:
                    ans += atom[3]
                    atoms.remove(atom)
 
    print(f'#{tc+1}', ans)

'''
<주의>
1. 원자 목록 순회 중 목록에 있는 배열 삭제 금지
2. 격자뿐만 아니라 가운데에서도 만날 수 있으므로 주의
3. 정수로만 계산하면 속도 높아짐
'''