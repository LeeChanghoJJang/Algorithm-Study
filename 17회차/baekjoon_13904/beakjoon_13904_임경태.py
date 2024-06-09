# 13904 과제

N = int(input())
hw_info = [list(map(int, input().split())) for _ in range(N)]
hw_list = [0] * 1001

# 점수 순 정렬
hw_info.sort(key=lambda x: -x[1])

# 과제 순회
for dl, score in hw_info:
    # 데드라인에서부터 앞으로 가면서 과제 배분
    for day in range(dl, 0, -1):
        if not hw_list[day]:
            hw_list[day] = score
            break

print(sum(hw_list))