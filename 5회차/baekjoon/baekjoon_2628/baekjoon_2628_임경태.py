import sys
sys.stdin = open('input.txt')

W, L = map(int, input().split())  # 가로, 세로
N = int(input())  # 잘라야하는 점선의 개수
w_cut, l_cut = [0, L], [0, W]
w_max, l_max = 0, 0

# 가로: 0, 점선번호 / 세로: 1, 점선 번호
for _ in range(N):
    d, n = map(int, input().split())
    if d: l_cut.append(n)
    else: w_cut.append(n)

w_cut.sort(); l_cut.sort()

for i in range(len(w_cut)-1):
    w_max = max(w_max, w_cut[i+1] - w_cut[i])

for i in range(len(l_cut)-1):
    l_max = max(l_max, l_cut[i+1] - l_cut[i])

print(w_max*l_max)