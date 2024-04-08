# 1450 냅색문제

N, C = map(int, input().split())
items = list(map(int, input().split()))


# 부분집합의 합 계산 함수
def subSetSum(arr):
    part = [0]
    for n in arr: part += [n+x for x in part]
    return part


# 두 부분으로 나누어 부분집합의 합 계산
part1 = subSetSum(items[:N//2])
part2 = subSetSum(items[N//2:])
part2.sort()  # 이진 탐색을 위해 정렬


# 한 부분의 부분집합의 합을 다른 부분과 대조하여 조건에 맞으면 카운트하는 함수
def countPairs(part1, part2, limit, cnt=0):
    for mass in part1:
        if mass > limit: continue
        L, R = 0, len(part2)

        # 기준점에 맞는 부분을 찾기 위한 이분탐색 부분
        while L < R:
            M = (L+R)//2
            if part2[M] + mass <= limit:
                L = M+1
            else:
                R = M
        # 조건을 맞추는 무게까지 개수 합산
        cnt += L

    return cnt


print(countPairs(part1, part2, C))