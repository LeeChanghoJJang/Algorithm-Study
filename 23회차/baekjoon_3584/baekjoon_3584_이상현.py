import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    parent = [0] * (N + 1)

    for _ in range(N - 1):
        A, B = map(int, input().split())
        parent[B] = A

    C, D = map(int, input().split())
    set_ = set()

    while True:
        if not C:
            break

        set_.add(C)
        C = parent[C]

    while True:
        if D in set_:
            print(D)
            break

        D = parent[D]