# 백준 1012번 유기농 배추

# 유기농 배추를 재배하기 위해 필요한 최소한의 지렁이 수를 구하는 문제
def dfs(x, y):
    # 범위를 벗어나면 함수 종료
    if not (0 <= x < m and 0 <= y < n):
        return False
    
    # 만약 현재 위치에 배추가 심어져 있으면 값을 0으로 바꿔주고(방문 처리)
    # 상하좌우를 모두 탐색하기 위해 재귀 호출
    if temp[y][x] == 1:
        temp[y][x] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        # 연결된 영역을 모두 탐색하면 True를 반환
        return True
    return False

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    temp = [[0] * m for _ in range(n)]
    
    # 지렁이의 좌표 입력
    for j in range(k):
        val1, val2 = map(int, input().split())
        temp[val2][val1] = 1
        
    result = 0
        
    for a in range(m):
        for b in range(n):
            # 연결된 영역의 개수를 구하는 과정
            if dfs(a, b):
                result += 1

    print(result)