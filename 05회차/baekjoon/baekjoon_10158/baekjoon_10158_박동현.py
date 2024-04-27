W,H = map(int,input().split())
P,Q = map(int,input().split())

move = int(input())

W_move = move % (2*W)
H_move = move % (2*H)

w = +1
for _ in range(W_move):
    P = P + w
    if P == W or P == 0:
        w *= -1

w = +1
for _ in range(H_move):
    Q = Q + w
    if Q == H or Q == 0:
        w *= -1

print(P,Q)