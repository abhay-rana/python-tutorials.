def move(maze,n,x,y,sol):
    if x>=n or y>=n or y<0 or x<0 :  #when i have not incuded myself
        return False
    if x==n-1 and y==n-1:   #base case for the recurrsion
        sol[x][y]=1         #cahnging the goal/destination to 1
        for e in sol:
            print(e)
        print()
        return True
    if maze[x][y]==0 or sol[x][y]==1:  #when there is a dead end
        return False
    sol[x][y]=1
    if move(maze,n,x,y+1,sol)==True: #move right   #recurrsion
        print("yes ")
        return True
    if move(maze,n,x,y-1,sol)==True: #move left
        print("yes2")
        return True
    if move(maze,n,x+1,y,sol)==True : #move down
        print("yes3")
        return True
    if move(maze,n,x-1,y,sol)==True:  #move top
        print("yes4")
        return True

    sol[x][y]=0

def sol(n):
    sol=[[0 for e in range(n)] for e in range(n)]
    print(move(maze,n,0,0,sol))

if __name__=="__main__":
    n=3
    maze=[[1,1,0],
          [1,1,0],
          [0,1,1]]
    sol(n)