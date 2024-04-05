n, k = map(int, input().split())
if n >= k:
    exit(print(0))

arr = list(map(int, input().split()))
tab = [0] * n
cnt = maximum = 0

# 안 쓰는 걸 먼저 뽑음
while arr:
    i = arr[0]

    # 있으면 pass
    if i in tab:
        arr.remove(i)
        continue

    # 멀티탭이 비었으면 꽂아줌
    elif 0 in tab:
        tab[tab.index(0)] = i
        arr.remove(i)
        continue

    # 멀티탭 full
    else:
        for mt in tab:
            # 쓸 예정이 없다면
            if mt not in arr:
                tmp = mt
                break

            # 다 쓸 예정이라면
            elif arr.index(mt) > maximum:
                maximum = arr.index(mt)
                tmp = mt

        tab[tab.index(tmp)] = i
        arr.remove(i)
        maximum = 0
        cnt += 1

print(cnt)
