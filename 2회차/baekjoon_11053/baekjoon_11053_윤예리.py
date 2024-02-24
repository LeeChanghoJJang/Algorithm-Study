N = int(input())
A = list(map(int, input().split()))
max_value = 0
ls = [0] * N    # 증가하는 개수

for i in range(N):
    ls[i] = 1
    for j in range(0, i):
        if A[j] < A[i] and ls[i] < ls[j] + 1:   # 작은 수 인지 확인 and 증가하는 순열인지 확인
            ls[i] = ls[j] + 1

print(max(ls))