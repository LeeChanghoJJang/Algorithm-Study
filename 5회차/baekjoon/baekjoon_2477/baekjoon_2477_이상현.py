K = int(input())
list_ = [tuple(map(int, input().split())) for _ in range(6)]
big, small = [], []

for i in range(1, 5):
    if sum(elem[0] == i for elem in list_) == 1:
        [big.append(elem[1]) for elem in list_ if elem[0] == i]
        small.append(list_[(list_.index((i, big[-1])) + 3) % 6][1])

print(K * (big[0] * big[1] - small[0] * small[1]))