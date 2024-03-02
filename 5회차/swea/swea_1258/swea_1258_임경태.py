import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    part_dict = {}  # key: width / value: length

    for i in range(n):
        width = 0
        for j in range(n):
            if arr[i][j] > 0:
                width += 1
            # width를 체크하던 상태에서 끝을 만나면 딕셔너리에 width를 key로 length를 증가시킴
            elif (not arr[i][j] or IndexError) and width:
                part_dict[width] = part_dict.get(width, 0) + 1
                width = 0

    # 우선 곱의 크기로 오름차순, 그 후 행이 작은 순으로 정렬
    part_list = sorted([(l, w) for w, l in part_dict.items()], key= lambda x: (x[0] * x[1], x[0]))

    print(f'#{tc+1}', len(part_dict), end=' ')
    for i in part_list:
        print(*i, end= ' ')
    print()
