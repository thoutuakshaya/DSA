import math

n=input("enter a number").split()
#it converts above to list
if len(n)==1 and n.isdigit():
    #conversion of list element to number
    n=int(n[0])
    original=n
    total=0
    while n!=0:
        rem=n%10
        quot=n//10
        total+=(rem*rem*rem)
        n=quot
    if total==original:
        print("is amgstrong",original)
    else:
        print("nooo not armstrong")

else:
    print("enter valid one")