dict_ = {}
total = 0

while True:
    try:
        name = input().strip()
    except EOFError:
        break

    if name in dict_:
        dict_[name] += 1
    else:
        dict_[name] = 1
    total += 1

list_ = list(dict_.items())
list_.sort(key = lambda x : x[0])

[print(f'{wood[0]} {round(wood[1] * 100 / total, 4):.4f}') for wood in list_]
