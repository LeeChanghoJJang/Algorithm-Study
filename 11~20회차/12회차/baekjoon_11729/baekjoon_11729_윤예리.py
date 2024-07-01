def hanoi(x, a, b, c):
    # 마지막
    if x == 1:
        print(a, c)
    else:
        # n-1개의 판을 B로 옮기기
        hanoi(x-1, a, c, b)
        # 제일 큰 판을 C로 옮기기
        print(a, c)
        # n-1개의 판을 B에서 C로 옮기기
        hanoi(x-1, b, a, c)

k = int(input())
print(2**k-1)
hanoi(k, 1, 2, 3)
