def check(x):
    if x == 1: return False

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False

    return True

def make_num(d, value):
    if d == n and check(int(value)):
        print(value)
        return

    for i in range(1, 10):
        if check(int(value+str(i))):
            make_num(d+1, value + str(i))

n = int(input())
make_num(0, '')