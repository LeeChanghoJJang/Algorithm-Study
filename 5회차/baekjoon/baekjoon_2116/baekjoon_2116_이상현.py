N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
dict_ = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}
max_ = 0

for b in range(1, 7):
    sum_ = 0
    
    for i in range(N):
        for j in range(6):
            if list_[i][j] == b:
                t = list_[i][dict_[j]]

                if b + t == 11:
                    sum_ += 4
                elif b == 6 or t == 6:
                    sum_ += 5
                else:
                    sum_ += 6
                b = t
                break

    max_ = max(max_, sum_)

print(max_)