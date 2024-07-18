# 트라이
# 계층 구조를 저장하는 방식

class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, folders):
        now = self.root
        for folder in folders:
            now = now.setdefault(folder,dict())

    def dfs(self, now, level=0):
        for nxt in sorted(now):
            print(" "*level + nxt)
            self.dfs(now[nxt], level+1)


trie = Trie()
for _ in range(int(input())):
    trie.insert(input().split("\\"))
trie.dfs(trie.root)
