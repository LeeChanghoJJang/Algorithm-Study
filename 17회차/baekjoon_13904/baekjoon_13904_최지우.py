import sys
input = sys.stdin.readline

N = int(input())
hw = [list(map(int, input().split())) for _ in range(N)]

hw.sort(key=lambda x:x[1])

day = [0 for _ in range(1001)]
result = 0

for _ in range(N):
    if not hw:
        break

    d, w = hw.pop()

    for i in range(d, 0, -1):
        if not day[i]:
            day[i] = 1
            result += w
            break
print(result)

'''
(d, w)
점수기준으로 정렬해놓고
최대 d에 넣기 반복
'''