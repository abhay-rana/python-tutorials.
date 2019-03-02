#fibonacci series with recurrsion
import time
start=time.time()
def fibo(n):
    #base case
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

for e in range(0,28):
    print(e,":",fibo(e))
end=time.time()
print("totoal time is:",end-start)