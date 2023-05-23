t=int(input())
for i in range(1,t+1):
    n=int(input())
    for j in range(1,n):
        if(n==j*j):
            print('True')
            break
    if(n!=j*j):
        print('False')