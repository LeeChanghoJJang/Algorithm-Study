import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    _, *A = input().split()
    _, *B = input().split()

    result1 = [(A.count('4'), A.count('3'), A.count('2'), A.count('1')),
            (B.count('4'), B.count('3'), B.count('2'), B.count('1'))]

    if result1[0] == result1[1]:
        print('D')
        continue

    result2 = sorted(result1)

    if result1 == result2:
        print('B')

    else:
        print('A')