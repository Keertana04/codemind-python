a=int(input())
b=int(input())
x=a+b
i=x
while(i>0):
    i=i+1
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        y=i
        break
print(y-x)