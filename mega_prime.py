def prime(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        return 1
c=0
c1=0
n=int(input())
if prime(n)==1:
    temp=n
    while(temp>0):
        r=temp%10
        c1+=1
        if prime(r)==1:
            c+=1
        temp//=10
    if c==c1:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")