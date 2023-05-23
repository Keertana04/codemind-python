a=list(map(int,input().split()))
b=list(map(int,input().split()))
count1=0
count2=0
for i in range (len(a)):
    for i in range (len(b)):
        if(a[i]<b[i]):
            count1+=1
        if(a[i]>b[i]):
            count2+=1
    print(count2,count1)
    break