def hanoi(n, from_, by, to):
    # 기저 사례: 원판이 없는 경우
    if n == 0:
        return

    # 가장 큰 원판을 제외한 나머지 원판들을 목적지가 아닌 임시 기둥으로 옮김
    hanoi(n - 1, from_, to, by)
    
    # 가장 큰 원판을 목적지로 옮김
    print(from_, to)
    
    # 임시 기둥에 옮겨놓은 나머지 원판들을 목적지로 옮김
    hanoi(n - 1, by, from_, to)

n = int(input())  # 옮길 원판의 개수 입력
print(2 ** n - 1)  # 원판을 옮기는 최소 횟수 출력
hanoi(n, 1, 2, 3)  # 하노이 탑을 옮기는 과정 출력
