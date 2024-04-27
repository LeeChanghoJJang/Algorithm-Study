# 1202 보석 도둑 (골드2)

from heapq import heappush, heappop

N, K = map(int, input().split())  # 보석 개수, 가방 개수
# 보석 무게, 보석 가격 (보석 무게에 대해 내림차순 정렬 - pop을 빠르게 하기 위해)
jwl = sorted([list(map(int, input().split())) for _ in range(N)], reverse=True)
ans, Q = 0, []

# 가방 가용 무게에 따라 오름차순 정렬
for w in sorted(int(input()) for _ in range(K)):
    # 가방에 담을 수 있는 무게까지의 가격을 우선순위 Q에 무게를 기준으로 내림차순 정렬
    while jwl and jwl[-1][0] <= w: heappush(Q, -jwl.pop()[1])
    if Q: ans -= heappop(Q)  # 제일 비싼 보석 당첨
    if not (Q or jwl): break

print(ans)

'''
106268KB / 1356ms
'''