n=int(input("enter number:"))
if n<0:
    print ("nill")
else:
    if (n%2)==0:
        print("even so print prime")
        p=n/2 #3rd prime there is array a of p elements a[p]
        a=[]
        m=0
        while(m==p):
            for i in range(2,int(m**0.5)+1):
                    if int(m%i)==0:
                        break
                    else:
                        a[i]=m
            m=m+1
                
          
                

    else:
        print("odd so fibonocii series")
        f=n/2+1