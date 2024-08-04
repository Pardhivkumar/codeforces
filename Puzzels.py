n,m=map(int,input("").split(" "))
ls=list(map(int,input("").split(" ")))
ls.sort()
least=ls[n-1]-ls[0]
for i in range(1,m-n+1):
    if((ls[i+n-1]-ls[i])<least):
        least=abs(ls[i+n-1]-ls[i])
print(least)