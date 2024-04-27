# 1343 폴리오미노

# 'AAAA'로 먼저 채워넣고 'BB'를 채워넣음
board = input().replace('XXXX', 'AAAA').replace('XX', 'BB')

# 'X'가 남아 있다면 -1 출력 / 아니라면 답 출력
if 'X' in board: print(-1)
else: print(board)

'''
31120KB / 40ms
replace(바꿀문자, 바꾼문자, 횟수(기본은 -1 > 전체))
'''