import sys
input = sys.stdin.readline

# 백준 7662번 이중 우선순위 큐

# heapq을 쓰지 않고 딕셔너리를 이용하여 풀어보려 했으나
# 계속 82%에서 시간초과...
T = int(input())

for tc in range(T):
    k = int(input())
    dict_ = {}

    for _ in range(k):
        command, num = input().split()
        num = int(num)

        if command == 'I':
            if num not in dict_:
                dict_[num] = 1
            else:
                dict_[num] += 1

        else:
            if not dict_:
                continue
            else:
                if num == 1:
                    temp = max(dict_.keys())

                    dict_[temp] -= 1

                    if not dict_[temp]:
                        del dict_[temp]
                else:
                    temp = min(dict_.keys())

                    dict_[temp] -= 1

                    if not dict_[temp]:
                        del dict_[temp]

    print(f'{max(dict_.keys())} {min(dict_.keys())}' if dict_ else 'EMPTY')