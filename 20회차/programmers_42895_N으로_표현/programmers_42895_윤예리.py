def solution(N, number):
    # [[5로 만들 수 있는 수 리스트], [55로 만들 수 있는 수 리스트], ...]
    dp = []

    for i in range(1, 9):
        # 5, 55, 555, ...
        cases = {int(str(N)*i)}

        for j in range(0, i-1):
            # dp[j] : j개의 N으로 만들 수 있는 수들의 집합
            for x in dp[j]:
                # dp[-j-1] : (i-1-j)개의 N으로 만들 수 있는 수들의 집합
                for y in dp[-j-1]:
                    cases.add(x+y)
                    cases.add(x-y)
                    cases.add(x*y)
                    if y: cases.add(x//y)

        if number in cases:
            return i
        dp.append(cases)
        
    return -1