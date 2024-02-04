# 11053 가장 긴 증가하는 부분 수열
# 부분문제에서 전체문제로 발전 -> DP
# 각 자리 숫자 별로 최대 길이로 만들 수 있는 수열을 고려

N = int(input())
A = list(map(int, input().split()))
# 최대로 이을 수 있는 길이에 대한 배열
max_len = [1] * N

# 수열 순회
for i in range(1, N):
    # 현재 숫자 이전까지 순회
    for j in range(i):
        # 현재 숫자보다 이전 숫자가 작다면
        if A[i] > A[j]:
            # 최대로 이을 수 있는 길이 선택
            max_len[i] = max(max_len[i], max_len[j]+1)

print(max(max_len))

'''
31120KB / 156ms
'''