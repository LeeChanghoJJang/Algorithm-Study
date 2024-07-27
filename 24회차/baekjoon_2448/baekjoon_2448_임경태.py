# 2448 별 찍기 - 11
def star(n):
    # 기본 삼각형 패턴 정의
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    
    # 재귀적으로 n//2 크기의 삼각형 패턴 생성
    stars = star(n // 2)
    
    # 머리 부분 삼각형 패턴 생성
    x = [' ' * (n // 2) + i + ' ' * (n // 2) for i in stars]
    
    # 몸 부분 삼각형 패턴 생성
    y = [i + ' ' + i for i in stars]
    
    # 머리와 몸 부분을 결합하여 반환
    return x + y

N = int(input())
result = star(N)
print('\n'.join(result))
