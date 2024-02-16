# 그래도 아직 DFS 쓰고 있으니까
def DFS(value, count) :
    global min_value
    start = [value]
    if value != 1 :
        now = start.pop()
        count += 1
        if min_value < count :      # 구문 없이는 시간초과 발생.
            return                  # min_value를 설정해 이미 count가 그 이상이면 바로 중단
        if now % 3 == 0 :           # 3으로 나눌 경우,
            start.append(now // 3)
        if now % 2 == 0 :
            start.append(now//2)    # 2로 나눌 경우
        if now > 1 :
            start.append(now-1)     # 1로 빼는 경우
        for next in start :
            DFS(next, count)        # 모두 담아서 재귀함수 시행
    else :                          # value가 1인 경우 (도착점)
        if min_value > count :      # count 비교 시행
            min_value = count

min_value = 1000
t = int(input())
DFS(t,0)
print(min_value)