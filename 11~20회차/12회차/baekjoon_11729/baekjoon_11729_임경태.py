# 11729 하노이탑 이동 순서
# 1 - 1 / 2 - 3 / 3 - 7 / 4 - 15 / 5 - 31

# 옮길 원판 개수, 시작 지점, 목표 지점
def move(n, start, end):
    if n == 1:
        print(start, end)
        return

    # 1단계 : n-1 개 원반 - 현재 기둥 -> 보조 기둥
    move(n-1, start, 6-start-end)
    # 2단계 : 제일 큰 원반 - 현재 기둥 -> 목표 기둥
    move(1, start, end)
    # 3단계 : n-1 개 원반 - 보조 기둥 -> 현재 기둥
    move(n-1, 6-start-end, end)

n = int(input())
print(2**n-1)
move(n, 1, 3)