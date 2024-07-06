def solution(land):
    answer = 0
    len_x = len(land)
    len_y = len(land[0])
    dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    num = 2
    cnt = {}
    
    for i in range(len_x):
        for j in range(len_y):
            if land[i][j] == 1:
                land[i][j] = num
                tmp = 1
                que = [(i, j)]
                while que:
                    x, y = que.pop()
                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len_x and 0 <= ny < len_y:
                            if land[nx][ny] == 1:
                                que.append((nx, ny))
                                land[nx][ny] = num
                                tmp += 1
                cnt[num] = tmp
                num += 1
    
    for i in range(len_y):
        tmp = set()
        x, y = 0, i
        
        while x < len_x:
            if land[x][i]:
                tmp.add(land[x][i])
            x += 1
            
        temp = 0
        for k in tmp:
            temp += cnt[k]
        
        answer = max(answer, temp)
    return answer