import sys

# 표준 입력을 'input.txt'에서 읽도록 리디렉션
sys.stdin = open('input.txt')

# N과 K를 입력에서 읽음
N, K = map(int, sys.stdin.readline().split())

# 단어를 저장할 리스트
word_list = []

# 각 단어의 고유한 문자를 저장할 리스트
set_word = []

# 단어를 읽고 해당하는 문자의 집합을 저장
for i in range(N):
    word_input = sys.stdin.readline().rstrip()
    set_word.append(set(list(word_input)))

# 문자가 학습되었는지 여부를 저장할 배열
learn = [0] * 26

# 기본적으로 학습해야 하는 문자들 (a, c, i, n, t)
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

# 읽을 수 있는 최대 단어 수를 저장할 변수
answer = 0

# 가능한 모든 문자 조합을 탐색하기 위한 DFS 함수
def dfs(idx, cnt):
    global answer

    # 학습한 문자의 수가 K - 5와 같으면 (이미 5개의 문자는 학습되어 있으며, 추가로 cnt개수만큼 학습)
    # 읽을 수 있는 단어를 확인
    if cnt == K - 5:
        readcnt = 0
        for word in set_word:
            check = True
            # 만약 학습하지 않은 단어가 하나라도 존재한다면 꽝
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            # 그 단어를 학습했다면 갯수에 +1
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    # 학습할 수 있는 모든 문자를 탐색
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

# K가 5보다 작으면 충분한 문자를 학습하여 어떤 단어도 읽을 수 없음
if K < 5:
    print(0)
# K가 26이면 모든 문자를 학습할 수 있으므로 읽을 수 있는 최대 단어 수는 N임
elif K == 26:
    print(N)
else:
    # DFS 함수를 호출하여 읽을 수 있는 최대 단어 수를 찾음
    dfs(0, 0)
    print(answer)
