def numbering(cnt, num):
    global max_, min_
    if cnt == k+1:
        if not min_:
            min_ = num
        else:
            max_ = num
        return

    for i in range(10):
        if not nums[i]:
            if cnt == 0 or check(num[-1], str(i), ineq[cnt-1]):
                nums[i] = 1
                numbering(cnt+1, num+str(i))
                nums[i] = 0


def check(x, y, z):
    if z == '>':
        return x > y
    else:
        return x < y


k = int(input())
ineq = list(map(str, input().split()))
nums = [0 for _ in range(10)]

max_ = ''
min_ = ''

numbering(0, '')

print(max_, min_)