# WE ARE MAKING A SODUKU SOLVER OF N*N GRID
# BY BACKTRACKING
# CHECK THERE IS NOT ANY CLASH BETWEEN row,column and a box

def chkrow(board,row,col,e):
    for i in range(4):
        if board[row][i]==e:
            return False
    return True

def chkcol(board,row,col,e):
    for i in range(4):
        if board[i][col]==e:
            return False
    return True

def chkbox(board,row,col,e):
    rowstart=row-row%2
    colstart=col-col%2
    for i in range(rowstart,rowstart+2):
        for j in range(colstart,colstart+2):
            if board[rowstart][colstart]==e:
                return False
    return True


def chkplace(board,row,col,e):
    if not chkrow(board,row,col,e):
        return False
    if not chkcol(board,row,col,e):
        return False
    if not chkbox(board,row,col,e):
        return False
    return True



def chkempty(board):
    col=-1
    row=-1
    isempty=False
    for i in range(4):
        for j in range(4):
            if board[i][j]==0:
                row=i
                col=j
                isempty=True
                break
        if isempty:
            break
    if not isempty:
        return True
    for e in range(1,5):
        if chkplace(board,row,col,e):
            board[row][col]=e
            if chkempty(board):
                return True
            board[row][col]=0 #backtracking
    return False
if __name__=="__main__":
    board=[[1,3,0,4],
           [2,0,3,1],
           [0,1,0,2],
           [4,0,1,0]]
    print(chkempty(board))
    # for each in board:
    #     print(each)
    for i in range(4):
        for e in range(4):
            print(board[i][e],end=" ")
        print()