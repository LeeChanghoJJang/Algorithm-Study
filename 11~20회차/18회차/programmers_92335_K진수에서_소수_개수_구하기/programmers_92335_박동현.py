# 소수 판정
def isprime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

def solution(n, k):
    answer = 0
    data = ""
    if n == 0:
        return 0
    # 진수 변환
    while n>0:
        data = str(n%k) + data
        n //= k
    # 0을 단위로 나눔
    number = data.split("0")
    print(number)
    # 소수 판정 (num이 빈 문자열"" 일수도 있기 때문에 num이 있는지도 함께 검증)
    for num in number :
        if num and isprime(int(num)):
            answer += 1
    # 반환
    return answer