def fibo(n):
    a,b=0,1
    for i in range(n):
        yield a
        #print(a,end=' ')
        a,b=b,a+b
n=int(input("enter number of steps"))
obj = fibo(10)
#print(next(obj))
for i in obj:
    print(i,end=' ')