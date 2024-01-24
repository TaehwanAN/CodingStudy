def solution(board):
    answer = 0
    ## 지뢰의 좌표를 찾는다 (x,y)
    mine_loc=[]
    for i,line in enumerate(board):
        for j,m in enumerate(line):
            if m == 1:
                mine_loc.append([i,j])
                
    # print(mine_loc)
    ## 위험구역을 -1로 바꾼다(x-1~x+1, y-1~y+1)
    for mine in mine_loc:
        for i in range(len(board)):
            for j in range(len(board)):
                if ((mine[0]-1 <= i) and (i <= mine[0]+1)and (mine[1]-1 <= j) and (j <= mine[1]+1)):
                    board[i][j]=-1
    # print(np.array(board))
    ## 안전지역 0 의 개수를 센다
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                answer+=1
    return answer