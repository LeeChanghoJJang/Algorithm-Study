# 백준 1343번 폴리오미노

# 사전순으로 가장 앞서는 답을 출력해야 하기 때문에 먼저 연속해 있는 4개의
# X가 있는지 확인하고 있으면 A로 replace, 그 후 2개의 연속해 있는 X가 있는지
# 확인 후 있으면 B로 replace
board = (input().replace('X' * 4, 'A' * 4).replace('X' * 2, 'B' * 2), -1)

# 만약 겹침없이 덮을 수 없으면 X가 board에 남아있음
print(board['X' in board[0]])