def sum(n):
    s=0
    temp=n
    while(temp):
        r=temp%10
        s=s+r
        temp=temp//10
    if(s>=10):
        sum(s)
    else:
        print(s)
n=int(input())
sum(n)