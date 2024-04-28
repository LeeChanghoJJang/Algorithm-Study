def dfs(idx, teach_cnt):
    global max_

    # 가르칠 수 있는 글자 수가 K - 5에 도달하면 단어의 개수를 세고 최댓값 갱신
    if teach_cnt == K - 5:
        cnt = 0

        # 모든 단어에 대해 가르쳐진 글자가 포함되어 있는지 확인하여 개수 세기
        for word in word_list:
            cnt += all(teach[ord(char) - ord('a')] for char in word)

        max_ = max(max_, cnt)
        return

    # idx부터 25까지의 알파벳에 대해 가르치지 않은 경우를 가르치고 재귀 호출
    for i in range(idx, 26):
        if not teach[i]:
            teach[i] = True
            dfs(i, teach_cnt + 1)  # 가르친 글자 수 증가
            teach[i] = False  # 백트래킹: 가르친 글자를 다시 되돌리고 다음 알파벳으로 이동

# 입력 받기
N, K = map(int, input().split())
word_list = [set(list(input())) for _ in range(N)]  # 단어 리스트 생성
teach = [False] * 26  # 각 알파벳을 가르쳤는지 여부를 저장하는 배열
max_ = 0

# 예외 처리: K가 5 미만이면 0 출력
if K < 5:
    print(0)
    exit()
# 예외 처리: K가 26이면 모든 알파벳을 가르칠 수 있으므로 단어의 개수 N 출력
if K == 26:
    print(N)
    exit()

# 'a', 'n', 't', 'i', 'c'은 무조건 가르쳐야 함
for char in 'antic':
    teach[ord(char) - ord('a')] = True

# dfs 호출하여 단어를 가르치고 최대 가르칠 수 있는 단어의 개수 구하기
dfs(0, 0)
print(max_)
