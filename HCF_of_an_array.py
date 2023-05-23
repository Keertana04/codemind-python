n=input()
a=list(map(int,input().split()))
for i in range(max(a),0,-1):
    c=0
    for j in a:
        if j%i==0:
            c+=1
    if(c==len(a)):
        print(i)
        break