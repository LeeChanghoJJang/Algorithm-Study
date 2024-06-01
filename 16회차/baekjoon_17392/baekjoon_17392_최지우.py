N, M = map(int, input().split())
arr = list(map(int, input().split()))

if sum(arr) >= M:
    ans = 0
else:
    vc = M
    now = i = 0

    while vc > 0:
        now -= 1
        if now <= -1:
            if i < N:
                now = arr[i]
                i += 1
            else:
                break
        vc -= 1
    cnt = vc

    ans = 0
    j = 1
    tmp = 1

    while j <= cnt:
        for i in range(N + 1):
            if j > cnt:
                break
            ans += tmp**2
            j += 1
        tmp += 1

print(ans)