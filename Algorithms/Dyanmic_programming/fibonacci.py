def fibonacci(n):
    if n<=2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# fibonacci(10)
# Using Memozation 
    # * Explicitly 
fibo_cache={}
def improved_fibo(n):
    if n<=2:
        return n
    if n in fibo_cache:
        return fibo_cache[n]
    else:
        value=improved_fibo(n-1)+improved_fibo(n-2)
        fibo_cache[n]=value
    return value
# print(improved_fibo(10))



from functools import lru_cache
@lru_cache(maxsize=1000)
def fibonacci1(n):
    if n<=2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci1(20))



def fibonacciModified(t1, t2, n):
    if n==1:
        return t1
    if n==2:
        return t2
    else:
        return fibonacciModified(t1,t2,n-1)**2+fibonacciModified(t1,t2,n-2)

print(fibonacciModified(0,1,5))