import sys
sys.stdin = open("input.txt")

# 상 하 좌 우
di = [0.5, -0.5, 0, 0]
dj = [0, 0, -0.5, 0.5]

t = int(input())
for tc in range(1, t+1):
    print(f'#{tc}', end=' ')
    n = int(input())
    total_energy = 0
    atom_list = [list(map(int, input().split())) for _ in range(n)]

    while len(atom_list) > 1:
        for atom in atom_list:
            d = atom[2]
            atom[0] += di[d]
            atom[1] += dj[d]

        visited = {}
        for atom in atom_list:
            try:
                visited[(atom[0], atom[1])].append(atom)
            except:
                visited[(atom[0], atom[1])] = [atom]

        # print(atom_list)
        atom_list = []
        for p in visited:
            # print(visited[p])
            if len(visited[p]) > 1:
                for atom in visited[p]:
                    total_energy += atom[3]
            else:
                ni = visited[p][0][0]
                nj = visited[p][0][1]

                if -1000 <= ni <= 1000 and -1000 <= nj <= 1000:
                    atom_list.append(visited[p][0])

    print(total_energy)