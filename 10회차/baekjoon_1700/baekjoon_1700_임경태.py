# 1700 멀티탭 스케줄링

N, K = map(int, input().split())
apps = list(map(int, input().split()))
tab, cnt = set(), 0

for i, app in enumerate(apps):
    # 멀티탭에 있으면 패스
    if app in tab: continue

    # 멀티탭에 공간이 있으면 꽂음
    if len(tab) < N: tab.add(app)
    else:
        # 꽂혀있는 코드 중 앞으로 언제 다시 사용할 지 체크
        use = [0] * 101
        for j, left_app in enumerate(apps[i:]):
            if not use[left_app] and left_app in tab:
                use[left_app] = j

        pop_app = 0
        for now_app in tab:
            # 앞으로 사용할 일이 없으면 뽑음
            if not use[now_app]: pop_app = now_app; break
            # 제일 마지막에 사용할 코드 뽑음
            if use[now_app] > use[pop_app]: pop_app = now_app

        tab.remove(pop_app)
        tab.add(app)
        cnt += 1

print(cnt)