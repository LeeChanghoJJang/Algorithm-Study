# 선공이 O, 후공이 X

def solution(board):
    def check(board) :
        tmp = set()
        # 일자
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] :
                if board[i][0]!=".":
                    tmp.add(board[i][0])
            if board[0][i] == board[1][i] == board[2][i] :
                if board[0][i]!=".":
                    tmp.add(board[0][i])
        # 대각선       
        if board[0][0] == board[1][1] == board[2][2] :
            if board[0][0] != ".":
                tmp.add(board[0][0])
        if board[0][2] == board[1][1] == board[2][0] :
            if board[0][2] != ".":
                tmp.add(board[0][2])
                
        # 승자가 한명인 경우 O 나 X 를 반환
        if len(tmp) == 1:
            return tmp.pop()
        # 그렇지 않은 경우 둘다 이겼다고 반환
        elif len(tmp) > 1:
            return "둘다 이겼어요"
        
         
    x_count = sum([row.count("X") for row in board])
    o_count = sum([row.count("O") for row in board])
    
    # 후공의 카운트가 더 많거나, 선공이 카운트가 2를 앞설 수는 없음
    if x_count > o_count or o_count-x_count >= 2: return 0
    
    # 결판이 난 경우
    # 1. 선공이 이긴 경우 후공보다 카운트가 높아야함
    # 2. 후공이 이긴 경우 선공과 카운트가 같아야함
    # 3. 둘다 이긴 경우는 존재할 수 없음
    res = check(board)
    if res :
        if res=="X":
            if x_count==o_count: return 1
            else : return 0
        elif res =="O":
            if o_count>x_count: return 1
            else : return 0
        elif res =="둘다 이겼어요": return 0
        
    # 모든 경우를 피했다면 정상적으로 진행중인 게임
    return 1