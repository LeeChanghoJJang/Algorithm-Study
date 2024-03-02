import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    a, *ap = map(int, input().split())
    b, *bp = map(int, input().split())

    for i in range(4, 0, -1):
        if ap.count(i) > bp.count(i): print('A'); break
        elif ap.count(i) < bp.count(i): print('B'); break
    else: print('D')