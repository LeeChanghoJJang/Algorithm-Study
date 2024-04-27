import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict_ = {}

for i in range(1, N + 1):
    pokemon = input().strip()
    dict_[pokemon] = i
    dict_[str(i)] = pokemon

for _ in range(M):
    target = input().strip()
    print(dict_[str(target)])