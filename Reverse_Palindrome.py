def rev(x):
    temp=x
    rev=0
    while(temp>0):
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    return rev
x=int(input())
x=x+rev(x)
while(1):
    if(x==rev(x)):
        print(x)
        break
    else:
        x=x+rev(x)