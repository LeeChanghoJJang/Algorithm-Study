# 비교 시 최소 값을 구하되, 겹치지 않아야함
# 전 항의 최소값을 계속 더하면서 내려가기

t = int(input())
test_list = [list(map(int,input().split())) for _ in range(t)]
# output_list = [[0 for _ in range(3)] for _ in range(t)]   # 첫번째 값을 더하는 과정이 더 복잡함

for i in range(1, t) :  # 앞의 리스트와 비교하여 값을 더해서 들어가기
    for j in range(3) : # 각 리스트 전 항의 인덱스가 겹치지 않는 최소값을 더해 리스트에 더함
        test_list[i][j] +=  min(test_list[i-1][(j+1)%3], test_list[i-1][(j+2)%3])   

print(min(test_list[-1]))