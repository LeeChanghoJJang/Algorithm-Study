def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discount = []

    def dfs(tmp, d):    # 할인 조합 구하기
        if d == len(tmp):
            discount.append(tmp[:])
            return

        for i in data:
            tmp[d] += i
            dfs(tmp, d+1)
            tmp[d] -= i
    dfs([0] * len(emoticons), 0)

    for d in discount:  # 할인 조합 돌면서 확인
        cnt = 0
        get = 0

        for i in users:
            pay = 0
            for j in range(len(d)):
                if i[0] <= d[j]:
                    pay += emoticons[j] * (100-d[j]) // 100
                if pay >= i[1]:
                    break

            if pay >= i[1]:     # 이모티콘 플러스 구매
                pay = 0
                cnt += 1
            get += pay

        if cnt >= answer[0]:
            if cnt == answer[0]:
                answer[1] = max(answer[1], get)
            else:
                answer[1] = get
            answer[0] = cnt

    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))