def calculate_original_expression(S):
    result = 0
    for i in range(len(S)):
        ai = int(S[i][:-1])  # 마지막 문자를 제외한 부분은 ai
        pi = int(S[i][-1])   # 마지막 문자는 pi
        result += ai ** pi
    return result

def main():
    T = int(input())

    for _ in range(T):
        n = int(input())
        S = input().split()

        result = calculate_original_expression(S)
        print(result)