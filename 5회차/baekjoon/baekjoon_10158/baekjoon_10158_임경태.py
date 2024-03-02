import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())  # 공간 크기
p, q = map(int, input().split())  # 초기 위치
t = int(input())  # 이동 시간

f = lambda x, w: x % w if not (x // w) % 2 else w - (x % w)

print(f(p + t, w), f(q + t, h))