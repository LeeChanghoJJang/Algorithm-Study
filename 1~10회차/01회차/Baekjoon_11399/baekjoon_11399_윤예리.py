N = int(input())
P_i = list(map(int, input().split()))

# 본 문제는
# (1) 개별 시간
# (2) 가중된 시간
# 의 합임.

# 따라서 (2)의 최소화가 필요함.
# (1은 이미 정해져 있기 때문)

# (2)를 최소화하려면
# 큰 수를 뒤로 보내야 함.
# 앞 순서일수록 많이 더해지기 때문임.

P2 = []
for i in P_i:       # [3, 1, 4, 3, 2]
    P2.append(i)    # P2라는 리스트에 P_i 값 복사
P2.sort()           # P2 오름차순 정렬
                    # [1, 2, 3, 3, 4]
arr = []
for j in range(len(P2)):         
    num = P_i.index(P2[j]) + 1      # P2의 값과 일치하는 P_i 의 인덱스를 num으로 받음
    arr.append(P_i[num-1])          # arr이라는 리스트에 찾은 값 넣기  
    P_i[num-1] = 0                  # 중복을 방지하기 위해 P_i에 찾은 값은 0으로 변환

time = []                       
for a in range(len(arr)):       # 값 별로 이전 값을 다 더하는 구간
    for b in range(a+1):        # range 특성 상 a+1 까지로 해야함
        time.append(arr[b])
print(sum(time))
