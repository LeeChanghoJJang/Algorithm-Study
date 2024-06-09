# 양과 늑대 (2022 KAKAO BLIND RECRUITMENT)

ans = 0

def solution(info, edges):
    visit = [1] + [0] * len(info)

    def BT(sheep, wolf):
        # 양보다 늑대가 적지 않다면 끝
        if sheep <= wolf:
            return

        global ans
        ans = max(ans, sheep)

        # 트리 순회
        for pnt, chd in edges:
            if visit[pnt] and not visit[chd]:
                visit[chd] = 1
                BT(sheep+1, wolf) if not info[chd] else BT(sheep, wolf+1)
                visit[chd] = 0

    BT(1, 0)
    return ans