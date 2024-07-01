# 2457 공주님의 정원
N = int(input())
flowers = sorted(list(map(int, input().split())) for _ in range(N))
now_end = (3, 1)
ans = 0

for i in range(N):
    # 각 꽃의 시작 월/일 및 끝 월/일
    sm, sd, em, ed = flowers[i]

    # 현재 커버 중인 기간에 포함되는 경우
    if (sm, sd) <= now_end < (em, ed):
        max_end = (em, ed)

        # 이후 꽃들을 순회하며 가장 긴 기간 찾기
        for nsm, nsd, nem, ned in flowers[i+1:N]:
            if now_end < (nsm, nsd): break
            max_end = max(max_end, (nem, ned))

        # 갱신
        now_end = max_end
        ans += 1

        # 11월 30일 이후까지 커버할 수 있다면 결과 출력 후 종료
        if now_end > (11, 30): exit(print(ans))

print(0) # 모든 꽃을 커버하지 못한 경우

'''
    핵심 : 주어진 데이터를 효율적으로 관리하고, 꽃이 개화하는 구간을 정확하게 파악하는 것
'''