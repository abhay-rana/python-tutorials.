def toh(n,source,helper,destination):
    if n==1:                                     #base case
        return print(f"---> {source} to {destination}")

    else:
        toh(n-1,source,destination,helper)      #recurrsive move n-1 discs from source to helper ro
        print(f"---> {source} to {destination}")     # move only nth disk from the source to destination
        toh(n-1,helper,source,destination)      #recurrsive move n-1 discs from helper rod to destination ro

toh(4,"A","B","C")