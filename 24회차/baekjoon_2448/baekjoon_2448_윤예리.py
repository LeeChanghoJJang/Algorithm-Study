n = int(input())

def sol(i):
    if i == 3:
        return ['  *  ', ' * * ', '*****']
    
    arr = sol(i//2)
    stars = []
    for j in arr:
        stars.append(' ' * (i//2) + j + ' ' * (i//2))

    for k in arr:
        stars.append(k + ' ' + k)
    
    return stars

print('\n'.join(sol(n)))