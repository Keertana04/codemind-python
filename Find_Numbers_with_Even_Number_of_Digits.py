n=int(input())
a=list(map(int,input().split()))
count2=0
for i in a:
    count=0
    temp=i
    while(temp):
        r=i%10
        count+=1
        temp=temp//10
    if count%2==0:
        count2+=1
print(count2)