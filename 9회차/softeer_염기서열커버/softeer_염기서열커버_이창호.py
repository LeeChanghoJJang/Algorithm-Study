import sys
sys.stdin = open('input.txt')

# 주어진 인덱스에 대한 슈퍼 DNA를 생성하는 함수
def genSuperDNA(index):
    loc = 0
    tempIndex = index
    while tempIndex % 2 == 0 :
        tempIndex //= 2
        loc +=1
    # 슈퍼 DNA는 이전 단계의 DNA를 합치는 것으로 생성됨
    superDNA[index] = merge(dna[loc],superDNA[index-2**loc])

# 두 DNA 시퀀스를 병합하는 함수
def merge(dna1,dna2):
    if not (dna1 and dna2):  # 둘 중 하나가 비어있으면 빈 리스트 반환
        return []
    dna = []
    for i in range(m):  # 두 DNA 시퀀스의 각 염기에 대해 병합 수행
        if dna1[i] == '.':
            dna.append(dna2[i])  # 첫 번째 시퀀스가 '.'인 경우, 두 번째 시퀀스를 사용
        elif dna2[i] == '.':
            dna.append(dna1[i])  # 두 번째 시퀀스가 '.'인 경우, 첫 번째 시퀀스를 사용
        elif dna1[i] == dna2[i]:
            dna.append(dna1[i])  # 두 시퀀스가 같은 경우 해당 염기를 사용
        else:
            return []  # 두 시퀀스가 다른 경우, 빈 리스트 반환
    return dna

# 입력 받기
n,m = map(int,input().split())
dna = [list(input()) for _  in range(n)]

# 슈퍼 DNA 생성
superDNA = [None for _ in range(2**n)]
superDNA[0] = ['.'] * m
for i in range(1,2**n):
    genSuperDNA(i)

# 주어진 인덱스에 대한 답을 생성하는 함수
def genAnswer(index):
    if answer[index] < n+1:
        return answer[index]
    bit1 = []
    number1 = number2 = 0
    tempIndex = index
    for i in range(n):
        if tempIndex % 2==1:
            bit1.append(i)
            number2 += 2**i
        tempIndex //=2
    digit = [0] * len(bit1)

    # 이진 플립 알고리즘을 사용하여 가능한 모든 조합을 계산
    for i in range(1,2**(len(bit1)-1)):
        for j in range(len(bit1)):
            if digit[j] == 1:
                digit[j] = 0
                temp = 2**bit1[j]
                number1 -= temp
                number2 += temp
            else:
                digit[j] = 1
                temp = 2**bit1[j]
                number1 += temp
                number2 -= temp
                break
        temp = genAnswer(number1) + genAnswer(number2)

        # 현재 답과 비교하여 최소값 갱신
        if answer[index] > temp:
            answer[index] = temp
    return answer[index]

# 답 생성 배열 초기화
answer = [n+1] * (2**n)
answer[0] = 0
for i in range(1,2**n):
    if superDNA[i] != []:
        answer[i] = 1
    else:
        genAnswer(i)

# 결과 출력
print(answer[2**n-1])
