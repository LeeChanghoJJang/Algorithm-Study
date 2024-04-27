import sys 
sys.stdin = open('input.txt') 


def merge(DNA1, DNA2):  # DNA[1] DNA[3] -> ['g', 'c', '.', '.', '.'] ['.', 'c', '.', 'a', 'g']
    # 두 염기서열 중 하나라도 비어있으면 빈 배열 반환
    if not (DNA1 and DNA2):
        return []
    DNA = []
    # 각 자리마다 커버하는 문자 추가
    for i in range(M):                  #  0 - 1 - 2 - 3 - 4
        if DNA1[i] == '.':              #          1   1   1
            DNA.append(DNA2[i])         #          .   a   g
        elif DNA2[i] == '.':            #  1
            DNA.append(DNA1[i])         #  g
        elif DNA1[i] == DNA2[i]:        #      1
            DNA.append(DNA1[i])         #      c
        else:
            return []
    return DNA                          #['g','c','.','a','g']


def gen_super_DNA(idx):                 # 예시: idx = 10
    pos = 0
    temp_idx = idx                      # temp_idx = 10

    # idx의 이진 표현에서 제일 오른쪽에 있는 1의 위치를 찾음
    while temp_idx % 2 == 0:            # result   = 0 - 1
        temp_idx //= 2                  # temp_idx = 5
        pos += 1                        # pos      = 1

    # 두 이진수를 기반으로 새로운 초염기서열 생성
    superDNA[idx] = merge(DNA[pos], superDNA[idx-2**pos])  # merge(DNA[1], superDNA[8] = DNA[3])


def gen_answer(idx):                    # 예시: idx = 9 / ans[idx] = N+1
    # 답이 구해졌으면 종료
    if ans[idx] < N+1:
        return ans[idx]

    bit = []
    num1 = num2 = 0
    temp_idx = idx

    # idx 이진 변환 수에서 1인 부분의 인덱스를 bit에 저장  9 - 4 - 2 - 1
    for i in range(N):                  # N = 4  i = 0 - 1 - 2 - 3
        if temp_idx % 2 == 1:           # result   = 1 - 0 - 0 - 1
            bit.append(i)               # append   = 0           3 -> bit = [0, 3]
            num2 += 2**i                # num2     = 1           8 -> num1 = 0 / num2 = 9
        temp_idx //= 2                  # temp_idx = 4 - 2 - 1 - 0

    digit = [0] * len(bit)              # len(bit) = 2

    # 가능한 모든 조합을 탐색하여 최소 염기서열 수를 찾음
    for i in range(1, 2**(len(bit)-1)): # i        = 1
        # 현재 부분집합에서 j번째 원소를 분해
        for j in range(len(bit)):       # j        = 0

            if digit[j] == 1:
                digit[j] = 0
                num1 -= 2**bit[j]
                num2 += 2**bit[j]
            else:                       # digit[j] = 0
                digit[j] = 1            # digit[j] = 1
                num1 += 2**bit[j]       # num1     = 1 -> num1 = 1
                num2 -= 2**bit[j]       # num2     = 1 -> num2 = 8
                break

        temp = gen_answer(num1) + gen_answer(num2)  # gen_answer(1) + gen_answer(8) = 1 + 1
        ans[idx] = min(ans[idx], temp)              # ans[9] = 2
    
    return ans[idx]  # ['a', '.', '.', 't', 't'], ['.', 'c', '.', 'a', 'g']


if __name__ == "__main__":
    N,M = map(int, input().split())
    DNA = [input() for _ in range(N)]

    # 초염기서열 배열과 초염기서열의 최소 개수 배열
    superDNA = [None for _ in range(2**N)]
    superDNA[0] = ['.'] * M
    ans = [N+1] * (2**N)
    ans[0] = 0

    # 초염기서열 생성
    for i in range(1, 2**N):
        gen_super_DNA(i)

    # 초염기서열의 최소 개수 체크
    for i in range(1, 2**N):
        if superDNA[i]:
            ans[i] = 1
        else:
            gen_answer(i)
    
    print(ans[-1])