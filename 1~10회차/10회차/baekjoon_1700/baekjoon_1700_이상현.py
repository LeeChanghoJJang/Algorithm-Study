N, K = map(int, input().split())
list_ = list(map(int, input().split()))
temp = set()
cnt = 0

for i, elem in enumerate(list_):
    if elem in temp:
        continue

    if len(temp) < N:
        temp.add(elem)
        continue

    cnt += 1
    dict_ = {}

    for j in range(i + 1, K):
        if list_[j] not in dict_ and list_[j] in temp:
            dict_[list_[j]] = j
            target = list_[j]

    for e in temp:
        if e not in dict_:
            target = e
            break
        if dict_[e] > dict_[target]:
            target = e

    temp.remove(target)
    temp.add(elem)

print(cnt)