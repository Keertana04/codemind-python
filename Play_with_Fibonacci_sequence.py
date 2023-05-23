def fib(n):
    a=0
    b=1 
    print(a,b,end=' ')
    for i in range (2,n):
    
        sum=a+b
        print(sum,end=' ')
        a=b
        b=sum
n=int(input())
fib(n)