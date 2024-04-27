# 2382 미생물 격리

from collections import defaultdict

def del_micro(kill):
    while kill:
        micro = kill.pop()
        if micro: micros.remove(micro)

def med(i):
    # 개체수 감소
    micros[i][2] //= 2
    # 군집 전멸
    if not micros[i][2]:
        return micros[i]
    # 방향 변환
    if micros[i][3] in (1, 3):
        micros[i][3] += 1
    else:
        micros[i][3] -= 1
    return

def merge(m):
    m.sort(key=lambda x: x[2])
    idx = micros.index(m[-1])
    micros[idx][2] = sum(i[2] for i in m)
    m.pop()
    return m

def move():
    kill, pos = [], defaultdict(list)
    # 이동
    for i in range(len(micros)):
        micros[i][0] += ds[micros[i][3]][0]
        micros[i][1] += ds[micros[i][3]][1]
        r, c = micros[i][0], micros[i][1]

        # 약품
        if not (0 < r < N-1 and 0 < c < N-1):
            kill.append(med(i))
        else:
            pos[(r, c)].append(micros[i])
    del_micro(kill)

    # 병합
    for micro in pos.values():
        if len(micro) > 1:
            kill.extend(merge(micro))
    del_micro(kill)

ds = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    micros = [list(map(int, input().split())) for _ in range(K)]
    for time in range(M):
        move()
    print(f"#{tc+1}", sum(micro[2] for micro in micros))