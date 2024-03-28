# 1620 나는야 포켓몬 마스터 이다솜

n, m = map(int, input().split())
pokemon_name = {}
pokemon_idx = {}

for i in range(1, n+1):
    char = input().strip()
    pokemon_name[char] = i
    pokemon_idx[i] = char

for _ in range(m):
    char = input().strip()
    if char.isdigit():
        print(pokemon_idx[int(char)])
    else:
        print(pokemon_name[char])