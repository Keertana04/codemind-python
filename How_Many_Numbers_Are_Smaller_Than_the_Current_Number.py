n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(n):
    count=0
    for j in range(n):
        if i!=j:
            if a[i]>a[j]:
                count+=1
    print(count,end=" ")