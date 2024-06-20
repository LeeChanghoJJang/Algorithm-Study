import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, k = map(int, input().split())
    score = list(map(int, input().split()))

    student = [0] * n
    for s in score:
        student[s-1] = 1

    for s in range(len(student)):
        if student[s] == 0:
            print(s+1, end=' ')
    print()