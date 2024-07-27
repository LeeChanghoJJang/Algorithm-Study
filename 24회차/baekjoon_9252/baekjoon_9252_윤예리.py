first = [""] + list(input())
second = [""] + list(input())

LCS = [[""] * len(second) for _ in range(len(first))]

for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]:
            LCS[i][j] = LCS[i-1][j-1] + first[i]

        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]

result = LCS[-1][-1]
print(len(result))
print(result)