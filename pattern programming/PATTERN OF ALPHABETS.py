# OUTER LOOP FOR THE ROWS
# INNER LOOP FOR THE COLUMNS
# ENTER THE NUMBER OF ROWS BY THE user
ascii_code=65
n=int(input("enter the number of rows"))
for e in range(n):
    for i in range(0,e):
        x=chr(ascii_code)
        print(x,end=" ")
        ascii_code+=1
    else:
        print(" ")

