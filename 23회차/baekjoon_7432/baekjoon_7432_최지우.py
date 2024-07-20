def drt(idx, dr):
    if idx < len(path):
        cur = path[idx]
    else:
        return
    if cur in dr:
        drt(idx+1, dr[cur])
    else:
        dr[cur] = {}
        drt(idx+1, dr[cur])
        

def print_tree(dr, indent=0):
    for key in sorted(dr.keys()):
        print(' ' * indent + key)
        print_tree(dr[key], indent + 1)


N = int(input())
diir = {}
for _ in range(N):
    path = list(input().strip().split('\\'))
    drt(0, diir)
            
print_tree(diir)

