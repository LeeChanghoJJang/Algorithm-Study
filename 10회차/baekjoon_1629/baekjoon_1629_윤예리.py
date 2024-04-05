# 왜 마지막에 나눠주는 것 보다 재귀함수에서 나눠주는 게 시간이 덜 걸리는 지 모르겠당
# dp로도 풀 수 있지 않을까? 라는 승민이 오빠야의 의견 전달드립니당.

# 모듈러 연산
def fpow(a, n):
    if n == 1:
        return a % c
    else:
        x = fpow(a, n//2)
        if not n % 2:
            return (x * x) % c
        else:
            return (x*x*a) % c

a, b, c = map(int, input().split())
print(fpow(a, b))