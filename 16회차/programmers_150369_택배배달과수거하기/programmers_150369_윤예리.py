def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries.reverse()
    pickups.reverse()

    d = p = 0
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]

        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n-i) * 2

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))