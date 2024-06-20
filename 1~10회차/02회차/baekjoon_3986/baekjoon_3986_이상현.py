# 백준 3986번 좋은 단어

N = int(input())
result = 0

# 스택을 이용하여 접근
for i in range(N):
    stack = []
    str_ = input()

    # 입력받은 문자열을 왼쪽에서 부터 순회
    for char_ in str_:

        # 만약 현재 스택에 가장 마지막에 들어있는 원소가 순회중인
        # 문자와 같으면 그 마지막 원소를 제거함
        if stack and char_ == stack[-1]:
            stack.pop()

        # 그렇지 않으면 순회중인 문자를 스택의 마지막에 추가함
        else:
            stack.append(char_)

    # 만약 입력받은 문자열이 좋은 단어라면 적절하게 짝을 지을 수 있으므로
    # 스택이 비어있어야 함
    if not stack:
        result += 1

print(result)