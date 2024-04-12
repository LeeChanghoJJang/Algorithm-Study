from itertools import combinations

def mbti_dist(a, b):
    result = 0

    for i in range(4):
        if a[i] != b[i]:
            result += 1
            
    return result

T = int(input())

for _ in range(T):
    N = int(input())
    list_ = input().split()
    min_ = 1000

    if N > 32:
        print(0)
    else:
        temp = combinations(list_, 3)

        for i, j, k in temp:
            dist_ = mbti_dist(i, j)
            dist_ += mbti_dist(j, k)
            dist_ += mbti_dist(k, i)

            min_ = min(min_, dist_)

        print(min_)