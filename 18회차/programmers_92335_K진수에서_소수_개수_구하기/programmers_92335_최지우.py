def solution(n, k):
    answer = 0
    kn = []
    while n > 0:
        kn.append(str(n%k))
        n //= k
    kn = ''.join(kn[::-1])
    kn_sp = kn.split('0')

    kn_sp = [x for x in kn_sp if x]

    def is_prime(num):
        if num <= 1:
            return False

        if num == 2:
            return True

        if not num%2:
            return False

        for i in range(3, int(num**(1/2))+1, 2):
            if not num%i:
                return False

        return True

    for i in kn_sp:
        if is_prime(int(i)):
            answer += 1

    return answer


n = 110011
k = 10
print(solution(n, k))