import math

def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def convert(n, q):
    tmp = ''

    while n>0:
        n, mod = divmod(n, q)
        tmp += str(mod)

    return tmp[::-1]

def solution(n, k):
    answer = 0

    n = convert(n, k)
    # print(n.split('0'))
    for i in n.split('0'):
        if i and is_prime(int(i)):
            answer += 1

    return answer

print(solution(437674, 3))
print(solution(110011, 10))