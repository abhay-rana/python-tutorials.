# N QUEEN P4ROBLEM N IS ENTER BY THE USER
global n
n=4

def printsolution(board):
    for i in range(n):
        for e in range(n):
           print(board[i][e],end=" ")
        print()

# A utility function(issafe) to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens

def issafe(board,row,col,n):
    ##check for the left side
    for e in range(col):
        if board[row][e]==1:
            return False

    ##check for the lefty diagnol
    ix,iy=row,col
    while ix>=0 and iy>=0:
        if board[ix][iy]==1:
            return False
        ix-=1
        iy-=1

    #check for the down left diagnol
    jx,jy=row,col
    while jx<n and jy>=0:
        if board[jx][jy]==1:
            return False
        jx+=1
        jy-=1

    return True

def nqueen(board,col):
    if col>=n:  #base case fir the termination of the recurrsion
        return True
    else:
        for i in range(0,n):#row
            if issafe(board,i,col,n):
                board[i][col]=1
                if nqueen(board,col+1)==True:
                    return True
                board[i][col]=0 #backtrack
        return False


if __name__=="__main__":
    n=4
    board=[[0 for e in range(4)] for i in range(4)]
    if nqueen(board,0)==False:
        print("there is no solution exit")
    printsolution(board)