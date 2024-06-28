def solution(N, number):
    DP = [set() for _ in range(9)]
    for i in range(1, 9):
        num = int(str(N)*i)
        DP[i].add(num)
        for j in range(1, i):
            for comb1 in DP[i - j]:
                for comb2 in DP[j]:
                    for num in comb1+comb2, abs(comb1-comb2), comb1*comb2, comb1//comb2, comb2//comb1:
                        if 1<=num<=32000:
                            DP[i].add(num)
        if number in DP[i] : return i
    return -1