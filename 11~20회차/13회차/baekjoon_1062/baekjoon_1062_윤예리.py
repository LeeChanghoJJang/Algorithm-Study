import sys
input = sys.stdin.readline

def dfs(i, cnt):
    global answer

    if cnt == k:
        num_of_word = 0
        for word in words:
            for w in word:
                if not visited[ord(w)-97]:
                    break
            else:
                num_of_word += 1

        answer = max(answer, num_of_word)
        return

    for j in range(i, 26):
        if not visited[j]:
            visited[j] = 1
            dfs(j, cnt+1)
            visited[j] = 0


n, k = map(int, input().split())
if k < 5:
    exit(print(0))
elif k >= 26:
    exit(print(n))
else:
    k -= 5

answer = 0
visited = [0] * 26
for i in ['a', 'c', 'i', 'n', 't']:
    visited[ord(i)-97] = 1

words = [set(input().strip()) for _ in range(n)]
dfs(0, 0)
print(answer)