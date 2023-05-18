p,r,t=map(int,input().split())
c=p*(1+r/100)**t
#print(round(c,2))
print("%.2f"%c)