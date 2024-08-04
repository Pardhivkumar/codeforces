t=int(input(""))
while(t>0):
    n=int(input(""))
    for i in range(2,30):
        temp=((2**i)-1)
        if(n%temp==0):
            print(n//temp)
            break
        else:
            continue
    t-=1