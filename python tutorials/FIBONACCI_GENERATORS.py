#fibonacci seires without the help of genertaors
import time
start=time.time()
def fibo(n):
    a,b,c=0,1,0
    while True:
        if c>n:
            return
        yield a
        a,b=b,a+b
        c+=1
end=time.time()
print(list(fibo(27)))
x=end-start
print("total time taken is:",x)


##generators are more fast than the recurrsion in this case of the fibonacci series
#after the 27th term the fibonaaci series with the recurrsion taken much time
# where as the fibonaaci series witrh generators just takes milliseconds