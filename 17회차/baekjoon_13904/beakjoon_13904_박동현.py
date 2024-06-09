import sys
input = sys.stdin.readline


N = int(input())
hw = []
for _ in range(N):
    data = tuple(map(int,input().split()))
    hw.append(data)


# 1. 큰 점수 부터 꺼내서 ans의 좌표에 넣어두기
# 2. ans의 인덱스를 day로 생각해서 그보다 작은 곳에 숫자 넣기
# 3. 넣어둔 수보다 더 큰 수가 들어오면 교체하기
# 최대치가 1000개라서 ans 크기 지정
### 최대치를 day의 최대값을 비교해서 만들 수도 있으나, 더 느림(44ms vs 36ms)
ans = [0] * 1001
hw.sort(key=lambda x : x[1], reverse=True)
for d,score in hw :
    while d>0:
        if ans[d]>=score:
            d-=1
        else :
            ans[d]=score
            break
print(sum(ans))
# 근데 이게 왜 우선순위 큐임..? 어디서 쓸지 모르겠는데