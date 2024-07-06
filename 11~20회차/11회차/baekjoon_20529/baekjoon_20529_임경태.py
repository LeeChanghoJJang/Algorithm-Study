# 20529 가장 가까운 세 사람의 심리적 거리

from itertools import combinations

for _ in range(int(input())):
    N, ans = int(input()), 8
    MBTI = input().split()

    # N이 32보다 크면 적어도 3개인 mbti가 있으므로 최소 거리는 0
    if N > 32: print(0); continue

    # 주어진 MBTI중에서 원소 개수가 3개인 조합 골라냄
    for a in set(combinations(MBTI, 3)):
        cnt = 0

        # 각 자리마다 set 글자 개수로 동일 문자 판별
        for b in map(set, zip(*a)):
            if len(b) == 2: cnt += 2

        # 답과 비교 후 최솟값 선정
        ans = min(ans, cnt)

    print(ans)