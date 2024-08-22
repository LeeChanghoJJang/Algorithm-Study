S = input()                     # 목표 문장

data = dict()                   # 문자: 문자열 길이
for _ in range(int(input())):
    a = input()
    data[a] = len(a)

length = len(S)

DP = [float("inf")]*(length+1)  # DP 배열
DP[0] = 0                       # 문자열 길이가 0일때 DP 값 0으로 설정 

for i in range(length+1):       # 1) DP 순회
    for char in data:           # 2) 문자 순회
        # DP 인덱스가 문자보다 짧은 경우 패스
        if i-data[char]<0:continue  
        # 정렬했을 때를 기준으로 지금 순회하고 있는 문자와 문장의 문자가 다르면 패스
        if sorted(char)!=sorted(S[i-data[char]:i]) : continue

        # 문자 위치가 다른 경우 tmp +1 
        tmp = 0
        for a,b in zip(char, S[i-data[char]:i]):
            if a!=b: tmp += 1

        # 계산된 tmp + 이전 DP값 vs DP에 이미 저장된 값
        DP[i] = min(DP[i], DP[i-data[char]]+tmp)
# 마지막 값이 아직 inf로 남아있다면 문장 구성이 안된다는 뜻 
print(DP[-1] if DP[-1] != float("inf") else -1)
