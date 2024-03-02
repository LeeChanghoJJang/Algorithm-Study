import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N = int(input())
    income = 0

    # 입력 받자마자 합산
    for i in range(N):
        value = tuple(map(int, list(input())))
        if i <= N//2:
            income += sum(value[N//2-i : N//2+i+1])
        else:
            income += sum(value[i-N//2 : 3*N//2-i])

    print(f"#{tc+1}", income)