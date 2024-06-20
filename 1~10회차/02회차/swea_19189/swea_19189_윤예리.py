def power(x, y, p):
    result = 1
    x = x % p

    while y > 0:
        if y % 2 == 1:
            result = (result * x) % p
        y = y // 2
        x = (x * x) % p
    return result


def count_beautiful_pairs(N, P):
    beautiful_pairs = 0

    for i in range(1, N + 1):
        beautiful_pairs = (beautiful_pairs + power(i, N - 1, P)) % P

    return beautiful_pairs


def main():
    TC = int(input("테스트 케이스의 수 입력: "))

    for _ in range(TC):
        N, P = map(int, input().split())
        result = count_beautiful_pairs(N, P)
        print(result)