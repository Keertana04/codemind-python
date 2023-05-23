n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
b.sort()
x=[]
for i in b:
    x.append(a.count(i))
x.sort()
x=x[::-1]
for i in x:
    for j in b:
        if i==a.count(j):
            print(j,end=" ")
            b.remove(j)
            break