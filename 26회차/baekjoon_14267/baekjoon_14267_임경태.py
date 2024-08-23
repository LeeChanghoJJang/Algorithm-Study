# 14267 회사 문화 1

n, m = map(int, input().split())
maps = [0] + list(map(int, input().split()))

good_stamp = [0] * (n+1)

# 칭찬 스티커 직원에게 할당
for _ in range(m):
    i, w = map(int, input().split())
    good_stamp[i] += w

# 사장은 항상 0개의 스티커를 받음
print('0', end=' ')

# 2번 직원부터 n번 직원까지 각자의 칭찬 스티커 수를 출력
for i in range(2, n+1):
    # 직속 상사의 칭찬 스티커에 자신의 칭찬 스티커를 더함
    good_stamp[i] += good_stamp[maps[i]]
    print(good_stamp[i], end=' ')