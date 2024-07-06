def solution(N, number):
    dp = [[]]

    x = 0
    for i in range(1, 9):
        dp.append(set())
        x = 10*x + N
        dp[i].add(x) # N, NN, NNN...

        for j in range(i):
            # 연산자 케이스
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)


            if number in dp[i]:
                return i

    return -1