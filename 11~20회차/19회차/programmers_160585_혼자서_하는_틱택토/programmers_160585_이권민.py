def solution(board):
  wins = [[[0,0], [0,1], [0,2]],
         [[1,0], [1,1], [1,2]],
         [[2,0], [2,1], [2,2]],
         [[0,0], [1,0], [2,0]],
         [[0,1], [1,1], [2,1]],
         [[0,2], [1,2], [2,2]],
         [[0,0], [1,1], [2,2]],
         [[2,0], [1,1], [0,2]]]

  # 승자 확인
  winner_list = []
  for win1, win2, win3 in wins:
    if board[win1[0]][win1[1]] == board[win2[0]][win2[1]] == board[win3[0]][win3[1]]:
      winner = board[win1[0]][win1[1]]
      if winner != '.':
        winner_list.append(winner)

  # O, X 각각의 개수
  o_num = sum(map(lambda x: x.count('O'), board))
  x_num = sum(map(lambda x: x.count('X'), board))

  # 3개가 연결된 개수가 2이상이거나 O, X 모두 완성된 경우
  if len(winner_list) > 2 or len(set(winner_list)) == 2:
    return 0
  # 승자가 O 또는 X인 경우
  elif len(winner_list) == 1:
    if winner_list[0] == 'O':
      return 1 if o_num == x_num + 1 else 0
    else:
      return 1 if o_num == x_num else 0
  # 승자가 없는 경우
  else:
    return 1 if o_num == x_num + 1 or o_num == x_num else 0