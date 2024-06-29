# 17299 오등큰수
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
F = Counter(A)
NGF = [-1] * N
S = []

for i in range(N-1, 0, -1):
    while S and F[A[i]] >= F[A[S[-1]]]: S.pop()

    if S: NGF[i] = A[S[-1]]

    S.append(i)

print(*NGF)

'''
    핵심 : 스택을 사용해 배열을 역순으로 처리하면서 다음 큰 빈도를 가진 요소를 효율적으로 찾는 것
'''