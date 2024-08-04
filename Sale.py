n,m=map(int,input("").split(" "))
ls=list(map(int,input("").split(" ")))
cc=0
a=[]
ls.sort()
for i in range(len(ls)):
    if(ls[i]<0):
        cc+=1
        temp=-1*ls[i]
        a.append(temp)
sum=0
if(cc<m):
    for i in range(len(a)):
        sum+=a[i]
    print(sum)   
else:
    for i in range(m):
        sum+=a[i]
    print(sum)