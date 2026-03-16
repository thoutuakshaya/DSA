n=int(input("enter first number: "))
m=int(input("enter second number: "))
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)   
print(gcd(n,m))
