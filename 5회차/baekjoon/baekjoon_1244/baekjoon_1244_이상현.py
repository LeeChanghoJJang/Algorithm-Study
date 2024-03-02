import sys
input = sys.stdin.readline

N = int(input())
s_list = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    g, num = map(int, input().split())

    if g == 1:
        for i in range(num - 1, N, num):
            s_list[i] = +(not s_list[i])

    elif g == 2:
        s_list[num - 1] = +(not s_list[num - 1])

        i = 1
        while 0 <= num - 1 - i and num - 1 + i < N and s_list[num - 1 - i] == s_list[num - 1 + i]:
            s_list[num - 1 - i] = +(not s_list[num - 1 - i])
            s_list[num - 1 + i] = +(not s_list[num - 1 + i])
            i += 1

for i in range(N):
    print(s_list[i], end = ' ')

    if i % 20 == 19:
        print()