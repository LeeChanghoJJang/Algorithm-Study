# 백준 1929번 소수 구하기
# 입력받은 M과 N 사이의 (M 이상, N이하)
# 소수를 모두 출력하는 문제

M, N = map(int, input().split())

prime = [0, 0, 1] + [1] * (N - 2)

# 소수이면 1, 소수가 아니면 0인 배열
for num in range(2, N + 1):
    if prime[num]:
    
        # 에라토스테네스의 체 사용
        for index in range(2 * num, N + 1, num):
            prime[index] = 0 


for num in range(M, N + 1):    
    if prime[num]:
        print(num)

# 위 코드의 시간 복잡도는 O(N * log(log N))
# 주어진 문제에서 N <= 1,000,000