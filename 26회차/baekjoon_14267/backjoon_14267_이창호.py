import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] + list(map(int, input().split()))
point = [0] * (n + 1)

for i in range(m):  # 입력받은 칭찬점수를 더해주는 부분
    u, cnt = map(int, input().split())
    point[u] += cnt

for i in range(2, n + 1):  # 직속상관의 칭찬점수를 더해주는 부분
    point[i] += point[parent[i]]

for i in range(1, len(point)):
    print(point[i], end=' ')