import sys
input = sys.stdin.readline

# 세 사람의 거리 계산
def check(str1, str2, str3):
    tmp = 0
    for i in range(4):
        if str1[i] != str2[i]:
            tmp += 1
        if tmp > dist:
            return
        if str2[i] != str3[i]:
            tmp += 1
        if tmp > dist:
            return
        if str3[i] != str1[i]:
            tmp += 1
        if tmp > dist:
            return
    return tmp

# 조합 계산
def cal():
    global dist

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                tmp = check(arr[i], arr[j], arr[k])
                if tmp:
                    dist = min(dist, tmp)
                if tmp == 0:    # 0이면 최소이므로 더 이상 계산할 필요 없음
                    dist = 0
                    return

T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(str, input().split()))
    dist = float('inf')
    cal()
    print(dist)