from itertools import combinations

def shoot(archer_list , enemy_set):
    global N, M, D

    cnt = 0
    while enemy_set:
        target_set = set()

        for archer in archer_list:
            target = 0
            min_ = 225

            for enemy in enemy_set:
                dist_ = N - enemy[0] + abs(archer - enemy[1])

                if dist_ <= D and dist_ < min_:
                    target = enemy
                    min_ = dist_
                elif dist_ <= D and dist_ == min_ and target[1] > enemy[1]:
                    target = enemy

            if target != 0:
                target_set.add(target)

        cnt += len(target_set)
        enemy_set = set([(row + 1, col) for row, col in enemy_set if row < N - 1 and (row, col) not in target_set])

    return cnt

N, M, D = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(N)]
enemy_list = []
max_ = 0

for row in range(N):
    for col in range(M):
        if list_[row][col]:
            enemy_list.append((row, col))

for case in combinations([n for n in range(M)], 3):
    archer_list = [col for col in case]
    max_ = max(max_, shoot(archer_list, set(enemy_list)))

print(max_)