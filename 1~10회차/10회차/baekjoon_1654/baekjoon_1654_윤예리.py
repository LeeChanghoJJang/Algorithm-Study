# 이분 탐색
def cnt(x):
    m = 0
    for i in range(k):
        m += len_lan[i] // x
    return m

def binary_search():
    global result
    start = 1
    end = max(len_lan)
    
    while start <= end:
        mid = (start + end) // 2

        if cnt(mid) >= n:
            if mid > result:
                result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)

k, n = map(int, input().split())
len_lan =[int(input()) for _ in range(k)]
result = 0
binary_search()