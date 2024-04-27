# 2357 최솟값과 최댓값

INF = float('inf')
N, M = map(int, input().split())

# 노드 개수 : 2N-1
maxTree = [0 for _ in range(2*N)]
minTree = [INF for _ in range(2*N)]

# 트리 삽입 : 우선 리프 노드에만 숫자들 삽입 (리프 노드 순서가 인덱스)
for i in range(N):
    num = int(input())
    maxTree[N+i] = num
    minTree[N+i] = num

# 트리 정렬 : 두 자식 노드의 숫자 크기를 비교하여 부모 노드에 올려보냄
for i in range(N-1, 0, -1):
    # i<<1 = 2*i / i<<1|1 = 2*i+1
    maxTree[i] = max(maxTree[i<<1], maxTree[i<<1|1])
    minTree[i] = min(minTree[i<<1], minTree[i<<1|1])

# 쿼리 수행 : a번째부터 b번째까지 중 최솟값, 최댓값 정수 구하기
for _ in range(M):
    a, b = map(int, input().split())
    a += N-1
    b += N-1
    maxV = 0
    minV = INF

    while a < b:
        # a번째 노드가 왼쪽 자식 노드인 경우 (a 인덱스: 홀수)
        if a & 1:
            maxV = max(maxV, maxTree[a])
            minV = min(minV, minTree[a])
            a += 1  # 다른 가지를 탐색하기 위해 (+)
        # b번째 노드가 오른쪽 자식 노드인 경우 (b 인덱스: 짝수)
        if ~(b & 1):
            maxV = max(maxV, maxTree[b])
            minV = min(minV, minTree[b])
            b -= 1  # 다른 가지를 탐색하기 위해 (-)
        # 부모 노드로 이동
        a >>= 1
        b >>= 1

    if a == b:
        maxV = maxTree[a]
        minV = minTree[a]

    print(minV, maxV)