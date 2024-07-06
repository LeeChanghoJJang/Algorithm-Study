# from itertools import combinations

# N = int(input())
# chu = [*map(int,input().split())]

# res = set()
# for i in range(1,N+1):
#     res.update(map(sum, combinations(chu,i)))
# i = 1
# while True :
#     if i in res :
#         i += 1
#     else :
#         exit(print(i))
# 모든 경우의 수를 계산하면 안됨


N = int(input())
chu = sorted([*map(int,input().split())])
ans = 0
# 작은 숫자부터 계산하면서,
for weight in chu:
    # 밑에서부터 더한 값이 지금 추의 무게보다 작다면, 중간에 비는 구간이 생길 수 밖에 없다
    if weight > ans + 1:break
    ans += weight
print(ans+1)