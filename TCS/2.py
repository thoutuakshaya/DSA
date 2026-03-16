#an=ar^n-1
#r=2 
#r=3

n=int(input())
if (n%2==0):
    #odd
    n=pow(3,(n//2)-1)
    print(n)
else:
    n=pow(2,(n-1)//2)
    print(n)