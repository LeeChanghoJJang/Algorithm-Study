# 2470 두 용액

# 풀이1 : 정렬 방식 (42036KB / 104ms)
N = int(input())
feat = sorted(map(int, input().split()), key=lambda x: abs(x))  # 용액의 절댓값 기준으로 정렬
min_v, temp = 1e+10, 0

for i in range(N-1):
    pls = abs(feat[i] + feat[i+1])  # 이웃한 두 수 비교
    if min_v > pls:
        min_v = pls; temp = i

print(min(feat[temp], feat[temp+1]), max(feat[temp], feat[temp+1]))


# 풀이2 : 투 포인터 방식 (42036KB / 104ms)
def tp():
    s, e = 0, -1
    min_v = abs(feat[s] + feat[e])
    ans = (feat[s], feat[e])

    while s < e:
        pls = feat[s] + feat[e]
        if min_v > abs(pls):
            min_v = abs(pls)
            ans = (feat[s], feat[e])
        # 인덱스 갱신
        if pls < 0: s += 1
        else: e -= 1

    return ans

N = int(input())
feat = sorted(map(int, input().split()))
print(*tp())