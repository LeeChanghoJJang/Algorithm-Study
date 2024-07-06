def solution(friends, gifts):
    answer = 0
    n = len(friends)
    gift_point = [0] * n
    arr = [[0] * n for _ in range(n)]
    friend_dict = {name: idx for idx, name in enumerate(friends)}

    for gift in gifts:
        from_, to = gift.split()
        gift_point[friend_dict[from_]] += 1
        gift_point[friend_dict[to]] -= 1

        arr[friend_dict[from_]][friend_dict[to]] += 1

    for base in friends:
        cnt = 0
        for target in friends:
            b, t = friend_dict[base], friend_dict[target]
            if b == t:
                continue

            if arr[b][t] > arr[t][b]:
                cnt += 1
                continue

            if arr[b][t] == arr[t][b]:
                if gift_point[b] > gift_point[t]:
                    cnt += 1
        answer = max(answer, cnt)
    return answer


f = ["a", "b", "c"]
g = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(f, g))